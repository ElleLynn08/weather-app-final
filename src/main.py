from dotenv import load_dotenv
import os
from src.weather_api_client import WeatherAPIClient
from datetime import datetime, timezone, timedelta
import socket

def format_date(date_obj, is_24_hour_format=True):
    """
    Formats a datetime object into a user-friendly date string.

    Parameters:
    date_obj (datetime): The datetime object to format.
    is_24_hour_format (bool): Whether to display the time in 24-hour format.

    Returns:
    str: Formatted date string.
    """
    day_of_week = date_obj.strftime("%A")
    date = date_obj.strftime("%d %b %Y")  # Shortened month format
    if is_24_hour_format:
        time = date_obj.strftime("%H:%M")
    else:
        time = date_obj.strftime("%I:%M %p")
    return f"{day_of_week}, {date}, and the time is {time}"

def display_forecast(forecast):
    """
    Displays a simplified 5-day forecast.

    Parameters:
    forecast (dict): The forecast data.
    """
    print("\n5-Day Weather Forecast:")
    days_shown = set()  # To keep track of unique days (no duplicates)
    for day in forecast["list"]:
        # Parse date and time from forecast data
        date = datetime.strptime(day["dt_txt"], "%Y-%m-%d %H:%M:%S")
        day_abbr = date.strftime("%a")  # Shortened weekday (e.g., Sun, Mon)
        if day_abbr not in days_shown:
            days_shown.add(day_abbr)  # Add day to set to avoid duplicates

            # Extract forecast details
            high_temp = round(day["main"]["temp_max"])
            low_temp = round(day["main"]["temp_min"])
            description = day["weather"][0]["description"].capitalize()
            icon_path = day["weather"][0].get("icon", "")  # Placeholder for icon path

            # Print the forecast
            print(f"{day_abbr}: {description}, High: {high_temp}°F, Low: {low_temp}°F, Icon: {icon_path}")
        
        if len(days_shown) == 5:  # Stop after 5 unique days
            break

def get_local_location():
    """
    Tries to get the local hostname or location for display purposes.

    Returns:
    str: Local hostname or a fallback string.
    """
    try:
        return socket.gethostname()  # Attempts to fetch local machine's hostname
    except Exception:
        return "your location"  # Fallback

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("API Key not found. Please set it in the .env file.")
        return

    client = WeatherAPIClient(api_key)
    city = input("Enter the name of a city to get the weather: ")

    # Fetch current weather
    current_weather = client.get_current_weather(city)
    if current_weather:
        # Get local time and location
        caller_time = datetime.now()
        local_location = get_local_location()
        print(f"\nYour local time and date is: {caller_time.strftime('%d %b %Y')} and the time is {caller_time.strftime('%I:%M %p')} in {local_location}")

        # Calculate and display city's local time
        timezone_offset = current_weather.get("timezone", 0)
        city_time = datetime.now(timezone.utc) + timedelta(seconds=timezone_offset)
        print(f"The current time and date in {city} is: {format_date(city_time, is_24_hour_format=False)}")

        # Display current weather
        print(f"\nWeather in {city}: {current_weather['weather'][0]['description'].capitalize()}")
        print(f"Temperature: {round(current_weather['main']['temp'])}°F")
    else:
        print("Could not fetch current weather data. Please check the city name or try again later.")

    # Fetch 5-day forecast
    forecast = client.get_5_day_forecast(city)
    if forecast:
        display_forecast(forecast)
    else:
        print("Could not fetch 5-day forecast data. Please check the city name or try again later.")

if __name__ == "__main__":
    main()









