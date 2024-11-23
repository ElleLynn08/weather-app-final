"""
This module defines the WeatherAPIClient for interacting with the OpenWeather API.
"""

import requests


class WeatherAPIClient:
    """
    A client for fetching current weather and 5-day forecast data using the OpenWeather API.
    """

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key):
        """
        Initializes the WeatherAPIClient with an API key.

        Parameters:
        api_key (str): The API key for authenticating with the OpenWeather API.
        """
        self.api_key = api_key

    def get_current_weather(self, city):
        """
        Fetches the current weather for a given city.

        Parameters:
        city (str): The city for which to fetch the weather data.

        Returns:
        dict: A dictionary with weather data if the request is successful; None otherwise.
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}?q={city}&appid={self.api_key}&units=imperial", 
                timeout=10  # Added timeout for better error handling
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            return None

    def get_5_day_forecast(self, city):
        """
        Fetches the 5-day weather forecast for a given city.

        Parameters:
        city (str): The city for which to fetch the weather data.

        Returns:
        dict: A dictionary with forecast data if the request is successful; None otherwise.
        """
        try:
            response = requests.get(
                f"{self.FORECAST_URL}?q={city}&appid={self.api_key}&units=imperial", 
                timeout=10  # Added timeout for better error handling
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            return None

    def get_icon_path(self, condition):
        """
        Maps weather conditions to animated SVG icon paths.

        Parameters:
        condition (str): The weather condition from OpenWeather API (e.g., "clear sky").

        Returns:
        str: Path to the corresponding SVG icon.
        """
        icon_map = {
            "clear sky": "static/icons/animated/day.svg",
            "few clouds": "static/icons/animated/cloudy-day-1.svg",
            "scattered clouds": "static/icons/animated/cloudy-day-2.svg",
            "broken clouds": "static/icons/animated/cloudy-day-3.svg",
            "shower rain": "static/icons/animated/rainy-3.svg",
            "rain": "static/icons/animated/rainy-5.svg",
            "thunderstorm": "static/icons/animated/thunder.svg",
            "snow": "static/icons/animated/snowy-1.svg",
            "mist": "static/icons/animated/weather_sunset.svg",
        }
        # Default icon if condition is not recognized
        return icon_map.get(condition.lower(), "static/icons/animated/weather.svg")
