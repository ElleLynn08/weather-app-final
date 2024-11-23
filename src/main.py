import os
from dotenv import load_dotenv
from src.weather_api_client import WeatherAPIClient

def main():
    """
    The main entry point for the Weather App.
    Fetches weather data for a city using the OpenWeather API.
    """
    # Load environment variables from .env
    load_dotenv()
    api_key = os.getenv("API_KEY")  # Fetch API key from .env

    if not api_key:
        print("API Key not found. Please set it in the .env file.")
        return

    client = WeatherAPIClient(api_key)
    city = input("Enter the name of a city to get the weather: ")
    weather = client.get_current_weather(city)

    if weather:
        # Convert temperature from Celsius to Fahrenheit and round to nearest whole number
        temp_fahrenheit = round(weather['main']['temp'] * 9/5 + 32)
        print(f"Weather in {city}: {weather['weather'][0]['description'].capitalize()}")
        print(f"Temperature: {temp_fahrenheit}°F")
    else:
        print("Could not fetch weather data. Please check the city name or try again later.")

if __name__ == "__main__":
    main()


