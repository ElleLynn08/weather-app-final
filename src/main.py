from dotenv import load_dotenv
import os
from src.weather_api_client import WeatherAPIClient
from src.patterns.history_manager import HistoryManager
from datetime import datetime, timezone, timedelta
import socket


def format_date(date_obj, is_24_hour_format=True):
    """
    Formats a datetime object into a user-friendly date string.

    Parameters:
    date_obj (datetime): The datetime object to format.
    is_24_hour_format (bool): Whether to use 24-hour format for the time.

    Returns:
    str: Formatted date string.
    """
    day_of_week = date_obj.strftime("%A")
    date = date_obj.strftime("%d %b %Y")
    time = date_obj.strftime("%H:%M") if is_24_hour_format else date_obj.strftime("%I:%M %p")
    return f"{day_of_week}, {date}, and the time is {time}"


def get_local_location():
    """
    Tries to get the local machine's hostname to show the caller's location.

    Returns:
    str: The hostname or a fallback message.
    """
    try:
        return socket.gethostname()
    except Exception:
        return "your location"


def display_forecast(forecast):
    """
    Displays a clean and simple 5-day forecast.

    Parameters:
    forecast (dict): The forecast data from the Weather API.
    """
    print("\n5-Day Weather Forecast:")
    for day in forecast["list"][:40:8]:  # Every 8th timestamp (8 timestamps per day)
        date = datetime.strptime(day["dt_txt"], "%Y-%m-%d %H:%M:%S")
        print(
            f"{date.strftime('%a')}: {day['weather'][0]['description'].capitalize()}, "
            f"High: {round(day['main']['temp_max'])}°F, "
            f"Low: {round(day['main']['temp_min'])}°F, "
            f"Icon: {day['weather'][0]['icon']}"
        )


def display_history(history):
    """
    Displays the saved weather history.

    Parameters:
    history (list): A list of saved weather history entries.
    """
    print("\nWeather History:")
    for entry in history:
        print(
            f"City: {entry['city']}, Date: {entry['date']}, "
            f"Weather: {entry['description']}, "
            f"Temp: {entry['temp']}°F"
        )


def main():
    """
    Main function to run the Weather App.
    Handles user input, fetches weather data, saves history, and displays it.
    """
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.getenv("API_KEY")  # Get the API key from the environment

    if not api_key:  # Check if the API key is missing
        print("API Key not found. Please set it in the .env file.")
        return

    # Initialize the Weather API client and the History Manager
    client = WeatherAPIClient(api_key)
    history_manager = HistoryManager()

    # Prompt the user to enter a city
    city = input("Enter the name of a city to get the weather: ")
    current_weather = client.get_current_weather(city)

    if current_weather:
        # Display the caller's current time
        caller_time = datetime.now()
        local_location = get_local_location()
        print(f"\nYour local time and date is: {caller_time.strftime('%d %b %Y')} and the time is {caller_time.strftime('%I:%M %p')} in {local_location}")

        # Calculate and display the city's local time
        timezone_offset = current_weather.get("timezone", 0)  # Get the timezone offset in seconds
        local_time = datetime.now(timezone.utc) + timedelta(seconds=timezone_offset)
        print(f"The current time and date in {city} is: {format_date(local_time, is_24_hour_format=False)}")

        # Display the current weather
        print(f"\nWeather in {city}: {current_weather['weather'][0]['description'].capitalize()}")
        print(f"Temperature: {round(current_weather['main']['temp'])}°F")

        # Save the current weather to the history
        history_manager.save({
            "city": city,
            "date": caller_time.strftime("%Y-%m-%d"),
            "description": current_weather['weather'][0]['description'].capitalize(),
            "temp": round(current_weather['main']['temp']),
        })

        # Fetch and display the 5-day forecast
        forecast = client.get_5_day_forecast(city)
        if forecast:
            display_forecast(forecast)

    # Prompt the user to view saved weather history
    print("\nWould you like to view weather history? (yes/no)")
    if input().lower() == "yes":
        display_history(history_manager.get_all())


if __name__ == "__main__":
    main()











