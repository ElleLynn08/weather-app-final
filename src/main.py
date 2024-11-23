from dotenv import load_dotenv
import os
from src.weather_api_client import WeatherAPIClient
from src.patterns.time_strategy import SystemTimeStrategy, LocalTimeStrategy
from datetime import datetime, timezone, timedelta

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
    date = date_obj.strftime("%d %B %Y")
    if is_24_hour_format:
        time = date_obj.strftime("%H:%M")
    else:
        time = date_obj.strftime("%I:%M %p")
    return f"Today is {day_of_week}, {date}, and the time is {time}"

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
        # Use strategies for time calculations
        system_time_strategy = SystemTimeStrategy()
        local_time_strategy = LocalTimeStrategy()

        # Fetch and print the caller's current time
        caller_time = datetime.now()
        print(f"\nYour current time and date is: {format_date(caller_time, is_24_hour_format=False)}")

        # Calculate and print the city's local time
        timezone_offset = current_weather.get("timezone", 0)
        local_time = datetime.now(timezone.utc) + timedelta(seconds=timezone_offset)
        print(f"Local time and date in {city} is: {format_date(local_time, is_24_hour_format=False)}")

        # Display weather
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








