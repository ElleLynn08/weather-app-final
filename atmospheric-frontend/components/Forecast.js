import React from 'react';

const Forecast = ({ forecast }) => {
  if (!forecast) {
    return <p style={{ textAlign: 'center', color: '#fff' }}>No forecast data available.</p>;
  }

  return (
    <div style={{ margin: '20px', textAlign: 'center' }}>
      <h3>5-Day Forecast</h3>
      <div style={{ display: 'flex', justifyContent: 'center', gap: '15px', flexWrap: 'wrap' }}>
        {forecast.list.slice(0, 5).map((day, index) => {
          const date = new Date(day.dt_txt);
          return (
            <div
              key={index}
              style={{
                backgroundColor: '#007bff',
                padding: '10px',
                borderRadius: '10px',
                color: '#fff',
                width: '120px',
                textAlign: 'center',
              }}
            >
              <p>{date.toLocaleDateString('en-US', { weekday: 'short' })}</p>
              <p>{Math.round(day.main.temp_max)}°F / {Math.round(day.main.temp_min)}°F</p>
              <img
                src={`http://openweathermap.org/img/wn/${day.weather[0].icon}@2x.png`}
                alt="weather icon"
                style={{ width: '50px' }}
              />
              <p>{day.weather[0].description}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Forecast;
