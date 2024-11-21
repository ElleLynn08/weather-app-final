import requests

class WeatherAPIClient:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, api_key):
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
                f"{self.BASE_URL}?q={city}&appid={self.api_key}&units=metric"
            )
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None
