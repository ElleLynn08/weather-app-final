import unittest
from unittest.mock import patch
from src.weather_api_client import WeatherAPIClient
import requests

class TestWeatherAPIClient(unittest.TestCase):

    @patch('src.weather_api_client.requests.get')
    def test_get_current_weather_success(self, mock_get):
        # Mock a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 77.0, "feels_like": 75.0, "humidity": 40},
            "wind": {"speed": 10.0},
            "name": "Paris"
        }
        
        client = WeatherAPIClient(api_key="test_key")
        response = client.get_current_weather("Paris")
        
        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(response["name"], "Paris")
        self.assertEqual(response["main"]["temp"], 77.0)
        self.assertEqual(response["main"]["feels_like"], 75.0)
        self.assertEqual(response["wind"]["speed"], 10.0)
        self.assertEqual(response["weather"][0]["description"], "clear sky")

    @patch('src.weather_api_client.requests.get')
    def test_get_current_weather_failure(self, mock_get):
        # Mock a failed response with an HTTPError
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError
        
        client = WeatherAPIClient(api_key="test_key")
        response = client.get_current_weather("InvalidCity")
        
        # Assertions
        self.assertIsNone(response)

    def test_get_icon_path(self):
        # Test the get_icon_path method directly
        client = WeatherAPIClient(api_key="test_key")
        self.assertEqual(client.get_icon_path("clear sky"), "static/icons/animated/day.svg")
        self.assertEqual(client.get_icon_path("thunderstorm"), "static/icons/animated/thunder.svg")
        self.assertEqual(client.get_icon_path("unknown condition"), "static/icons/animated/weather.svg")

if __name__ == "__main__":
    unittest.main()

