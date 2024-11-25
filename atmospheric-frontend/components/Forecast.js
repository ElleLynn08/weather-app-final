import React from 'react';
import './Forecast.css';

const Forecast = ({ forecast }) => {
  if (!forecast) {
    return <p className="forecast-no-data">No forecast data available.</p>;
  }

  return (
    <div className="forecast-container">
      <h3>5-Day Forecast</h3>
      <div className="forecast-list">
        {forecast.list.slice(0, 5).map((day, index) => {
          const date = new Date(day.dt_txt);
          return (
            <div className="forecast-day" key={index}>
              <p className="forecast-day-name">
                {date.toLocaleDateString('en-US', { weekday: 'short' })}
              </p>
              <p className="forecast-temp">
                {Math.round(day.main.temp_max)}°F / {Math.round(day.main.temp_min)}°F
              </p>
              <img
                className="forecast-icon"
                src={`http://openweathermap.org/img/wn/${day.weather[0].icon}@2x.png`}
                alt="weather icon"
              />
              <p className="forecast-description">{day.weather[0].description}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Forecast;

