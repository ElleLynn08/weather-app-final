from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

# Initializing the Flask app and enabling CORS for cross-origin requests
app = Flask(__name__)
CORS(app)  # This allows the frontend to communicate with the backend easily.

# Load environment variables (this is where we grab the API key from .env)
load_dotenv()
API_KEY = os.getenv("API_KEY")

# A quick safety check to ensure the API key is available
if not API_KEY:
    raise ValueError("API_KEY not found in the environment variables. Did you forget to add it?")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Handles requests for current weather data. Requires 'city' as a query parameter.
    Example: /weather?city=London&units=imperial
    """
    city = request.args.get('city')  # Grabbing the city from the request
    units = request.args.get('units', 'imperial')  # Defaults to imperial if not specified

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        # Sending a request to OpenWeather API for current weather
        response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units={units}")
        response.raise_for_status()  # Raise an error if the request fails
        data = response.json()

        # Adding the weather icon to the response for convenience
        icon_code = data['weather'][0]['icon']
        data['icon_url'] = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        return jsonify(data)  # Return the weather data
    except requests.exceptions.RequestException as e:
        # Handle errors gracefully and return a message for debugging
        return jsonify({"error": "Failed to fetch weather data", "details": str(e)}), 500

@app.route('/forecast', methods=['GET'])
def get_forecast():
    """
    Handles requests for a 5-day weather forecast. Requires 'city' as a query parameter.
    Example: /forecast?city=London&units=imperial
    """
    city = request.args.get('city')
    units = request.args.get('units', 'imperial')  # Defaults to imperial if not specified

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        # Sending a request to OpenWeather API for the 5-day forecast
        response = requests.get(f"{FORECAST_URL}?q={city}&appid={API_KEY}&units={units}")
        response.raise_for_status()
        data = response.json()
        return jsonify(data)  # Return the forecast data
    except requests.exceptions.RequestException as e:
        # Again, we handle errors nicely for troubleshooting
        return jsonify({"error": "Failed to fetch forecast data", "details": str(e)}), 500

if __name__ == '__main__':
    # Running the app in debug mode (for development only, not for production!)
    app.run(debug=True)

