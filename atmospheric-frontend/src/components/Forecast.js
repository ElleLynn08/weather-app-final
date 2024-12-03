import React from "react";
import "./Forecast.css";

const Forecast = ({ forecast, unitSystem, timezoneOffset }) => {
  if (!forecast || !Array.isArray(forecast) || forecast.length === 0) {
    return <p className="forecast-no-data">No forecast data available</p>;
  }

  const unitLabels = {
    temp: unitSystem === "imperial" ? "°F" : "°C",
  };

  const getDailyForecast = () => {
    if (timezoneOffset === undefined || timezoneOffset === null) {
      console.error("Invalid timezoneOffset:", timezoneOffset);
      return [];
    }

    const dailyForecastMap = {};

    forecast.forEach((entry) => {
      if (!entry.dt || typeof entry.dt !== "number") {
        console.error("Invalid dt value in forecast entry:", entry);
        return;
      }

      // Adjust timestamp for local time using timezoneOffset (in seconds)
      const adjustedTimestamp = entry.dt + timezoneOffset;
      const localDate = new Date(adjustedTimestamp * 1000)
        .toISOString()
        .split("T")[0]; // Extract YYYY-MM-DD format

      if (!dailyForecastMap[localDate]) {
        dailyForecastMap[localDate] = [];
      }
      dailyForecastMap[localDate].push(entry);
    });

    // Map daily forecast data
    const dailyForecast = Object.keys(dailyForecastMap).map((date) => {
      const dayForecasts = dailyForecastMap[date];
      let tempMax = -Infinity;
      let tempMin = Infinity;
      const weatherCount = {};

      dayForecasts.forEach((entry) => {
        const temp = entry.main?.temp;
        if (temp > tempMax) tempMax = temp;
        if (temp < tempMin) tempMin = temp;

        const weatherMain = entry.weather[0]?.main;
        if (weatherMain) {
          weatherCount[weatherMain] = (weatherCount[weatherMain] || 0) + 1;
        }
      });

      // Get the most frequent weather condition of the day
      const mostFrequentWeather = Object.keys(weatherCount).reduce((a, b) =>
        weatherCount[a] > weatherCount[b] ? a : b
      );

      const representativeEntry = dayForecasts.find(
        (entry) => entry.weather[0]?.main === mostFrequentWeather
      );

      return {
        date,
        tempMax,
        tempMin,
        weather: representativeEntry?.weather[0],
      };
    });

    // Filter out today and start from the next day
    const today = new Date().toISOString().split("T")[0];
    return dailyForecast.filter((day) => day.date > today);
  };

  const dailyForecast = getDailyForecast();

  return (
    <div className="forecast-container">
      <h3 className="forecast-header">5-Day Forecast</h3>
      <div className="forecast-list">
        {dailyForecast.slice(0, 5).map((day, index) => (
          <div key={index} className="forecast-day">
            <p className="forecast-day-name">
              {new Date(day.date).toLocaleDateString("en-US", {
                weekday: "short",
                month: "short",
                day: "numeric",
              })}
            </p>
            {day.weather ? (
              <>
                <img
                  className="forecast-icon"
                  src={`https://openweathermap.org/img/wn/${day.weather.icon}@2x.png`}
                  alt={day.weather.description}
                />
                <p className="forecast-temp">
                  {Math.round(day.tempMax)}
                  {unitLabels.temp} / {Math.round(day.tempMin)}
                  {unitLabels.temp}
                </p>
              </>
            ) : (
              <p>No weather data available for this day</p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Forecast;


































