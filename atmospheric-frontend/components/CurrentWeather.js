import React from 'react';

const CurrentWeather = ({ weather }) => {
  if (!weather) {
    return <p style={{ textAlign: 'center', color: '#fff' }}>No weather data available.</p>;
  }

  const { name, main, weather: weatherDetails, wind } = weather;

  return (
    <div style={{ textAlign: 'center', margin: '20px' }}>
      <h2>{name}</h2>
      <h3>{Math.round(main.temp)}°F</h3>
      <p>{weatherDetails[0].description}</p>
      <p>Feels Like: {Math.round(main.feels_like)}°F</p>
      <p>Wind: {wind.speed} mph</p>
      <p>Humidity: {main.humidity}%</p>
    </div>
  );
};

export default CurrentWeather;
