import React, { useState, useEffect } from 'react';
import CurrentWeather from './components/CurrentWeather';
import './App.css'; // Ensure you have styles here

const App = () => {
  // State for toggles
  const [unitSystem, setUnitSystem] = useState("imperial"); // 'imperial' or 'metric'
  const [timeFormat, setTimeFormat] = useState("12-hour"); // '12-hour' or '24-hour'
  const [weatherData, setWeatherData] = useState(null); // State for fetched weather data
  const [city, setCity] = useState(""); // City input state
  const [error, setError] = useState(""); // State for handling API errors

  // Function to fetch weather data
  const fetchWeatherData = async () => {
    if (!city) {
      setError("Please enter a city to search.");
      return;
    }
    setError(""); // Clear previous error
    try {
      const response = await fetch(
        `http://localhost:5000/weather?city=${city}&units=${unitSystem}`
      );
      if (!response.ok) {
        throw new Error("Failed to fetch weather data. Please try again.");
      }
      const data = await response.json();
      setWeatherData(data);
    } catch (err) {
      setError(err.message);
    }
  };

  // Toggle between Imperial and Metric
  const toggleUnitSystem = () => {
    setUnitSystem((prev) => (prev === "imperial" ? "metric" : "imperial"));
  };

  // Toggle between 12-hour and 24-hour formats
  const toggleTimeFormat = () => {
    setTimeFormat((prev) => (prev === "12-hour" ? "24-hour" : "12-hour"));
  };

  return (
    <div className="app">
      <header>
        <h1>Atmospheric: 5-Day Weather</h1>
        <div className="toggles">
          <button onClick={toggleUnitSystem}>
            {unitSystem === "imperial" ? "Switch to Metric" : "Switch to Imperial"}
          </button>
          <button onClick={toggleTimeFormat}>
            {timeFormat === "12-hour" ? "Switch to 24-hour" : "Switch to 12-hour"}
          </button>
        </div>
      </header>
      <main>
        <div className="search-bar">
          <input
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            placeholder="Enter a city..."
          />
          <button onClick={fetchWeatherData}>Search</button>
        </div>
        {error && <p style={{ color: "red", textAlign: "center" }}>{error}</p>}
        <CurrentWeather
          weather={weatherData}
          unitSystem={unitSystem}
          timeFormat={timeFormat}
        />
      </main>
    </div>
  );
};

export default App;


