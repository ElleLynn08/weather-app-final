import React from "react";
import "./CurrentWeather.css";

const CurrentWeather = ({ weather, unitSystem, sweetComment }) => {
  const unitLabels = {
    temp: unitSystem === "imperial" ? "°F" : "°C",
    speed: unitSystem === "imperial" ? "mph" : "kph",
    distance: unitSystem === "imperial" ? "miles" : "km",
  };

  return (
    <div className="current-weather">
      {/* Weather icon */}
      <img
        className="weather-icon"
        src={`http://openweathermap.org/img/wn/${weather.weather[0].icon}@4x.png`}
        alt={weather.weather[0].description}
      />

      {/* Weather description */}
      <p className="weather-description">
        {weather.weather[0].description.charAt(0).toUpperCase() +
          weather.weather[0].description.slice(1)}
      </p>

      {/* Temperature */}
      <h2 className="temperature">
        {Math.round(weather.main.temp)}
        {unitLabels.temp}
      </h2>

      {/* Dynamic Sweet Message */}
      <p className="message">{sweetComment}</p>

      {/* Weather details */}
      <div className="weather-details">
        <p>
          Feels Like: {Math.round(weather.main.feels_like)}
          {unitLabels.temp}
        </p>
        <p>Humidity: {weather.main.humidity}%</p>
        <p>
          Wind: {Math.round(weather.wind.speed)} {unitLabels.speed}
        </p>
        <p>
          Visibility: {weather.visibility / 1000} {unitLabels.distance}
        </p>
        <p>
          High: {Math.round(weather.main.temp_max)}
          {unitLabels.temp} / Low: {Math.round(weather.main.temp_min)}
          {unitLabels.temp}
        </p>
      </div>
    </div>
  );
};

export default CurrentWeather;























