from dotenv import load_dotenv
import os
from src.weather_api_client import WeatherAPIClient

def main():
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
        print(f"Weather in {city}: {weather['weather'][0]['description'].capitalize()}")
        print(f"Temperature: {weather['main']['temp']}°C")
    else:
        print("Could not fetch weather data. Please check the city name or try again later.")

if __name__ == "__main__":
    main()

