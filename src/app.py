"""
Flask application for serving weather and forecast data.
Provides endpoints to fetch weather data and a 5-day forecast for a given city.
"""

import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
TIMEZONEDB_API_KEY = os.getenv("TIMEZONEDB_API_KEY")

# Validate API keys
if not API_KEY:
    print("Error: OPENWEATHER_API_KEY is not set in the environment variables.")
    exit(1)

if not TIMEZONEDB_API_KEY:
    print("Error: TIMEZONEDB_API_KEY is not set in the environment variables.")
    exit(1)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Endpoint to get current weather data for a city.
    Query Parameters:
        city (str): The name of the city.
        units (str): The measurement units (default: imperial).

    Returns:
        JSON: Weather data for the city.
    """
    city = request.args.get('city')
    units = request.args.get('units', 'imperial')

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        response = requests.get(
            f"{BASE_URL}?q={city}&appid={API_KEY}&units={units}",
            timeout=10,  # Added timeout to prevent hanging requests
        )
        response.raise_for_status()
        weather_data = response.json()

        lat, lon = weather_data["coord"]["lat"], weather_data["coord"]["lon"]
        timezone_response = requests.get(
            f"http://api.timezonedb.com/v2.1/get-time-zone"
            f"?key={TIMEZONEDB_API_KEY}&format=json&by=position&lat={lat}&lng={lon}",
            timeout=10,
        )
        timezone_response.raise_for_status()
        timezone_data = timezone_response.json()

        if timezone_data.get("status") == "OK":
            weather_data["timeZoneName"] = timezone_data["zoneName"]
            weather_data["gmtOffset"] = timezone_data["gmtOffset"]
        else:
            print(f"Failed to fetch timezone data for {city}.")  # Debug log

        return jsonify(weather_data)
    except requests.RequestException as e:
        print(f"Error while fetching weather data: {e}")
        return jsonify({"error": "Failed to fetch weather data", "details": str(e)}), 500


@app.route('/forecast', methods=['GET'])
def get_forecast():
    """
    Endpoint to get 5-day weather forecast for a city.
    Query Parameters:
        city (str): The name of the city.
        units (str): The measurement units (default: imperial).

    Returns:
        JSON: Forecast data for the city.
    """
    city = request.args.get('city')
    units = request.args.get('units', 'imperial')

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        response = requests.get(
            f"{FORECAST_URL}?q={city}&appid={API_KEY}&units={units}",
            timeout=10,
        )
        response.raise_for_status()
        forecast_data = response.json()
        return jsonify(forecast_data)
    except requests.RequestException as e:
        print(f"Error while fetching forecast data: {e}")
        return jsonify({"error": "Failed to fetch forecast data", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
