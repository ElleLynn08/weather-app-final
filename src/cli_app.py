import os
import requests
from dotenv import load_dotenv


# Load the .env file from the main project directory
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=os.path.join(project_dir, '.env'))

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found. Please add it to your .env file.")


class HistoryManager:
    """
    Manages weather history, including saving, retrieving, and clearing entries.
    """
    def __init__(self):
        self.history = []

    def save(self, city_name, weather):
        """
        Save a weather entry to the history.
        """
        entry = {
            "city": city_name,
            "description": weather["description"],
            "temperature": weather["temperature"]
        }
        if entry not in self.history:  # Avoid duplicates
            self.history.append(entry)

    def view(self):
        """
        View all saved weather history.
        """
        if not self.history:
            print("No history available.")
        else:
            print("Weather History:")
            for i, entry in enumerate(self.history, start=1):
                print(f"{i}. {entry['city']}: {entry['description']}, {entry['temperature']}°F")
            print("-" * 40)

    def clear(self):
        """
        Clear all weather history.
        """
        self.history.clear()
        print("History cleared!")

def fetch_weather(city_name):
    """
    Fetch current weather data for the given city using OpenWeather API.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=imperial"
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return {
            "city": weather_data["name"],
            "description": weather_data["weather"][0]["description"],
            "temperature": weather_data["main"]["temp"]
        }
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")

def main():
    """
    Command-line interface for the weather app.
    """
    history_manager = HistoryManager()
    print("Welcome to the Weather App!")
    while True:
        print("Options:")
        print("1. Get weather for a city")
        print("2. View weather history")
        print("3. Clear history")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            city = input("Enter the name of a city: ").strip()
            weather = fetch_weather(city)
            if weather:
                print(f"Weather in {weather['city']}: {weather['description']}")
                print(f"Temperature: {weather['temperature']}°F")
                print("-" * 40)
                history_manager.save(city, weather)
        elif choice == "2":
            history_manager.view()
        elif choice == "3":
            history_manager.clear()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
