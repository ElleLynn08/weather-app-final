"""
Main module for weather application.
Fetches current weather, displays forecast, and saves weather history.
"""

import os
from datetime import datetime, timezone, timedelta
import socket
from dotenv import load_dotenv
from src.weather_api_client import WeatherAPIClient
from src.patterns.history_manager import HistoryManager


def format_date(date_obj, is_24_hour_format=True):
    """
    Formats a datetime object into a friendly date and time string.

    Args:
        date_obj (datetime): The datetime object to format.
        is_24_hour_format (bool): Whether to use 24-hour format.

    Returns:
        str: Formatted date and time string.
    """
    day_of_week = date_obj.strftime("%A")  # Example: Monday
    date = date_obj.strftime("%d %b %Y")  # Example: 24 Nov 2024
    time = date_obj.strftime("%H:%M") if is_24_hour_format else date_obj.strftime("%I:%M %p")
    return f"{day_of_week}, {date}, and the time is {time}"


def get_local_location():
    """
    Fetches the machine's hostname.

    Returns:
        str: The hostname or default location string.
    """
    try:
        return socket.gethostname()
    except OSError:  # Specific exception for socket errors
        return "your location"


def display_forecast(forecast):
    """
    Displays a simple 5-day weather forecast.

    Args:
        forecast (dict): Forecast data containing weather information.
    """
    print("\n5-Day Weather Forecast:")
    for day in forecast["list"][:40:8]:  # Grabbing every 8th timestamp (one per day)
        date = datetime.strptime(day["dt_txt"], "%Y-%m-%d %H:%M:%S")
        print(
            f"{date.strftime('%a')}: {day['weather'][0]['description'].capitalize()}, "
            f"High: {round(day['main']['temp_max'])}°F, "
            f"Low: {round(day['main']['temp_min'])}°F, "
            f"Icon: {day['weather'][0]['icon']}"
        )


def display_history(history):
    """
    Displays weather history saved by the user.

    Args:
        history (list): List of dictionaries containing weather history.
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
    Main function that initializes the application and handles user interactions.
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("API Key not found. Please set it in the .env file.")
        return

    # Initialize the Weather API client and history manager
    client = WeatherAPIClient(api_key)
    history_manager = HistoryManager()

    city = input("Enter the name of a city to get the weather: ")
    current_weather = client.get_current_weather(city)

    if current_weather:
        caller_time = datetime.now()
        local_location = get_local_location()
        print(f"\nYour local time is: {caller_time.strftime('%I:%M %p')} in {local_location}")

        timezone_offset = current_weather.get("timezone", 0)  # Timezone offset in seconds
        local_time = datetime.now(timezone.utc) + timedelta(seconds=timezone_offset)
        print(f"The time in {city} is: {format_date(local_time, is_24_hour_format=False)}")

        print(f"\nWeather in {city}: {current_weather['weather'][0]['description'].capitalize()}")
        print(f"Temperature: {round(current_weather['main']['temp'])}°F")

        # Save the weather data to history
        history_manager.save({
            "city": city,
            "date": caller_time.strftime("%Y-%m-%d"),
            "description": current_weather['weather'][0]['description'].capitalize(),
            "temp": round(current_weather['main']['temp']),
        })

        # Get the 5-day forecast and display it
        forecast = client.get_5_day_forecast(city)
        if forecast:
            display_forecast(forecast)

    # Ask if the user wants to view history
    print("\nWould you like to view weather history? (yes/no)")
    if input().lower() == "yes":
        display_history(history_manager.get_all())


if __name__ == "__main__":
    main()
