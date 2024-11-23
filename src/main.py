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

    # Initialize the weather client
    client = WeatherAPIClient(api_key)

    while True:
        # Ask for city input
        city = input("Enter the name of a city to get the weather (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye!")
            break

        # Fetch the current weather
        weather = client.get_current_weather(city)

        if weather:
            # Extract weather condition and get the icon path
            condition = weather['weather'][0]['description']
            icon_path = client.get_icon_path(condition)

            # Display weather details
            print(f"\nWeather in {city.title()}: {condition.capitalize()}")
            print(f"Temperature: {round(weather['main']['temp'])}°F")
            print(f"Feels Like: {round(weather['main']['feels_like'])}°F")
            print(f"Humidity: {weather['main']['humidity']}%")
            print(f"Wind Speed: {round(weather['wind']['speed'])} mph")
            print(f"Icon: {icon_path}\n")

        else:
            print("\nCould not fetch weather data. Please check the city name or try again later.\n")

if __name__ == "__main__":
    main()




