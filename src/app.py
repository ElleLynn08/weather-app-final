from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "your_openweather_api_key"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    units = request.args.get('units', 'imperial')  # Default to imperial if not provided

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        # Fetch data from OpenWeather API
        response = requests.get(
            f"{BASE_URL}?q={city}&appid={API_KEY}&units={units}"
        )
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
