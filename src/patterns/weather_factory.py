class WeatherDataFactory:
    @staticmethod
    def create_weather_data(data_type, data):
        """
        Factory method to create weather data objects based on the type.
        """
        if data_type == "current":
            return CurrentWeather(data)
        elif data_type == "forecast":
            return ForecastWeather(data)
        elif data_type == "historical":
            return HistoricalWeather(data)
        else:
            raise ValueError("Invalid weather data type")


class CurrentWeather:
    def __init__(self, data):
        self.data = data

    def display(self):
        # Convert temperature to Fahrenheit
        temp_f = round(self.data['main']['temp'] * 9/5 + 32, 1)
        print(f"Current weather: {self.data['weather'][0]['description'].capitalize()}")
        print(f"Temperature: {temp_f}°F")


class ForecastWeather:
    def __init__(self, data):
        self.data = data

    def display(self):
        print("5-day Forecast:")
        for day in self.data["list"][:5]:  # Limit to 5 days
            # Convert temperature to Fahrenheit and wind speed to mph
            temp_f = round(day['main']['temp'] * 9/5 + 32, 1)
            feels_like_f = round(day['main']['feels_like'] * 9/5 + 32, 1)
            wind_mph = round(day['wind']['speed'] * 2.237, 1)  # Convert m/s to mph
            print(f"Date: {day['dt_txt']}")
            print(f"  Temp: {temp_f}°F, Feels like: {feels_like_f}°F")
            print(f"  Humidity: {day['main']['humidity']}%, Wind: {wind_mph} mph")
            print(f"  Conditions: {day['weather'][0]['description'].capitalize()}\n")


class HistoricalWeather:
    def __init__(self, data):
        self.data = data

    def display(self):
        print("Last 5 days:")
        for day in self.data:
            # Convert temperature to Fahrenheit
            avg_temp_f = round(day['avg_temp'] * 9/5 + 32, 1)
            avg_feels_like_f = round(day['avg_feels_like'] * 9/5 + 32, 1)
            print(f"Date: {day['date']}")
            print(f"  Avg Temp: {avg_temp_f}°F, Avg Feels Like: {avg_feels_like_f}°F")





