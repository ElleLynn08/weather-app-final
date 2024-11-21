import unittest
from unittest.mock import patch
from src.weather_api_client import WeatherAPIClient
import requests

class TestWeatherAPIClient(unittest.TestCase):

    @patch('src.weather_api_client.requests.get')
    def test_get_current_weather_success(self, mock_get):
        # Set up the mock to return a specific response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 25.0},
            "name": "Paris"
        }
        
        client = WeatherAPIClient(api_key="test_key")
        response = client.get_current_weather("Paris")
        
        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(response["name"], "Paris")
        self.assertEqual(response["main"]["temp"], 25.0)

    @patch('src.weather_api_client.requests.get')
    def test_get_current_weather_failure(self, mock_get):
        # Mock a failed request by raising an HTTPError
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError
        
        client = WeatherAPIClient(api_key="test_key")
        response = client.get_current_weather("InvalidCity")
        
        # The method should return None if the city is invalid
        self.assertIsNone(response)

if __name__ == "__main__":
    unittest.main()
