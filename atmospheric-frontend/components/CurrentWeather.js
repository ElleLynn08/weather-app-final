import React from 'react';

const CurrentWeather = ({ weather, unitSystem, timeFormat }) => {
  if (!weather) {
    return <p style={{ textAlign: 'center', color: '#fff' }}>No weather data available.</p>;
  }

  const { name, main, weather: weatherDetails, wind, visibility } = weather;

  // Convert visibility based on unit system
  const visibilityDistance =
    unitSystem === "imperial"
      ? `${(visibility / 1609.344).toFixed(1)} miles`
      : `${(visibility / 1000).toFixed(1)} km`;

  // Format time based on timeFormat
  const formatTime = (date) => {
    const options = {
      hour: "numeric",
      minute: "numeric",
      hour12: timeFormat === "12-hour",
    };
    return new Intl.DateTimeFormat("en-US", options).format(new Date(date));
  };

  // Generate the sweet automated message based on the weather
  const getAutomationMessage = () => {
    const description = weatherDetails[0].description.toLowerCase();
    if (description.includes("rain")) {
      return "Don't forget your umbrella! Stay dry! ☔";
    } else if (description.includes("clear")) {
      return "It's a beautiful day! Enjoy the sunshine! 🌞";
    } else if (description.includes("cloud")) {
      return "Looks like a cozy, cloudy day. ☁️";
    } else if (description.includes("snow")) {
      return "Brrr! It's snowy out there. Stay warm! ❄️";
    } else {
      return "Hope your day is as wonderful as you are! ✨";
    }
  };

  return (
    <div style={{ textAlign: 'center', margin: '20px' }}>
      <h2>{name}</h2>
      <h3>{Math.round(main.temp)}°{unitSystem === "imperial" ? "F" : "C"}</h3>
      <p>{weatherDetails[0].description}</p>
      <p>Feels Like: {Math.round(main.feels_like)}°{unitSystem === "imperial" ? "F" : "C"}</p>
      <p>Wind: {wind.speed} {unitSystem === "imperial" ? "mph" : "km/h"}</p>
      <p>Humidity: {main.humidity}%</p>
      <p>Visibility: {visibilityDistance}</p>

      {/* Automated message */}
      <p style={{ marginTop: "20px", fontStyle: "italic", color: "#007acc" }}>
        {getAutomationMessage()}
      </p>
    </div>
  );
};

export default CurrentWeather;

