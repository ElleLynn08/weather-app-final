from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

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
    city = request.args.get('city')
    units = request.args.get('units', 'imperial')

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        # Fetch weather data
        response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units={units}")
        if response.status_code == 404:
            return jsonify({"error": f"City '{city}' not found."}), 404
        response.raise_for_status()
        weather_data = response.json()

        # Fetch timezone info using latitude and longitude
        lat = weather_data["coord"]["lat"]
        lon = weather_data["coord"]["lon"]
        timezone_response = requests.get(
            f"http://api.timezonedb.com/v2.1/get-time-zone?key={TIMEZONEDB_API_KEY}&format=json&by=position&lat={lat}&lng={lon}",
            timeout=10  # Add a timeout to prevent long wait times
        )
        timezone_response.raise_for_status()
        timezone_data = timezone_response.json()

        if timezone_data.get("status") == "OK":
            weather_data["timeZoneName"] = timezone_data["zoneName"]
            weather_data["gmtOffset"] = timezone_data["gmtOffset"]
            print(f"City: {city}, GMT Offset: {timezone_data['gmtOffset']}")  # Debug log
        else:
            print(f"Failed to fetch timezone data for {city}.")  # Debug log

        return jsonify(weather_data)
    except Exception as e:
        print(f"Error while fetching data: {str(e)}")  # Debug log
        return jsonify({"error": "Failed to fetch weather data", "details": str(e)}), 500

@app.route('/forecast', methods=['GET'])
def get_forecast():
    city = request.args.get('city')
    units = request.args.get('units', 'imperial')

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        response = requests.get(f"{FORECAST_URL}?q={city}&appid={API_KEY}&units={units}")
        if response.status_code == 404:
            return jsonify({"error": f"City '{city}' not found."}), 404
        response.raise_for_status()
        forecast_data = response.json()
        return jsonify(forecast_data)
    except Exception as e:
        print(f"Error while fetching forecast data: {str(e)}")  # Debug log
        return jsonify({"error": "Failed to fetch forecast data", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)







