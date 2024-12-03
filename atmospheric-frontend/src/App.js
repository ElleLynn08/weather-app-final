import React, { useState, useEffect, useCallback, useMemo } from "react";
import { DateTime } from "luxon"; // Luxon for time handling
import CurrentWeather from "./components/CurrentWeather";
import Forecast from "./components/Forecast";
import "./App.css";
import { getSweetMessage } from "./components/WeatherMessages";

const App = () => {
  const [unitSystem, setUnitSystem] = useState("imperial");
  const [timeFormat, setTimeFormat] = useState("12-hour");
  const [weatherData, setWeatherData] = useState(null);
  const [forecastData, setForecastData] = useState(null);
  const [city, setCity] = useState("");
  const [error, setError] = useState("");
  const [searchTriggered, setSearchTriggered] = useState(false);

  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || "";

  const fetchWeatherData = useCallback(
    async (queryCity, units) => {
      try {
        const response = await fetch(
          `${API_BASE_URL}/weather?city=${queryCity}&units=${units}`
        );
        if (!response.ok) throw new Error("Failed to fetch weather data.");
        const data = await response.json();
        setWeatherData(data);
        setError("");
      } catch (err) {
        console.error(err.message);
        setError("City not found. Please enter a valid city.");
      }
    },
    [API_BASE_URL]
  );

  const fetchForecastData = useCallback(
    async (queryCity, units) => {
      try {
        const response = await fetch(
          `${API_BASE_URL}/forecast?city=${queryCity}&units=${units}`
        );
        if (!response.ok) throw new Error("Failed to fetch forecast data.");
        const data = await response.json();
        setForecastData(data.list);
        setError("");
      } catch (err) {
        console.error(err.message);
        setError("City not found. Please enter a valid city.");
      }
    },
    [API_BASE_URL]
  );

  const handleSearch = () => {
    if (city.trim() !== "") {
      setSearchTriggered(true);
      fetchWeatherData(city, unitSystem);
      fetchForecastData(city, unitSystem);
    }
  };

  useEffect(() => {
    if (searchTriggered) {
      fetchWeatherData(city, unitSystem);
      fetchForecastData(city, unitSystem);
    }
  }, [fetchWeatherData, fetchForecastData, searchTriggered, city, unitSystem]);

  const toggleUnitSystem = () =>
    setUnitSystem((prev) => (prev === "imperial" ? "metric" : "imperial"));
  const toggleTimeFormat = () =>
    setTimeFormat((prev) => (prev === "12-hour" ? "24-hour" : "12-hour"));

  // Function to get the local hour
  const getLocalHour = (timezoneOffset) => {
    if (timezoneOffset === undefined || timezoneOffset === null) {
      return null;
    }
    const utcDateTime = DateTime.utc();
    const localDateTime = utcDateTime.plus({ seconds: timezoneOffset });
    return localDateTime.hour; // Returns hour in 24-hour format (0-23)
  };

  // Determine if it's nighttime using useMemo
  const isNightTime = useMemo(() => {
    if (weatherData?.timezone !== undefined) {
      const localHour = getLocalHour(weatherData.timezone);
      console.log(`Local hour in ${weatherData.name}: ${localHour}`);
      const isNight = localHour >= 21 || localHour < 6; // Nighttime between 9 PM and 6 AM
      console.log(`Is it nighttime in ${weatherData.name}? ${isNight}`);
      return isNight;
    }
    return false;
  }, [weatherData]);

  // Updated getFormattedDateTime function using Luxon
  const getFormattedDateTime = (timezoneOffset, formatType) => {
    if (timezoneOffset === undefined || timezoneOffset === null) {
      return "Time zone not available";
    }

    const localDateTime = DateTime.utc().plus({ seconds: timezoneOffset });

    const formatString =
      formatType === "time"
        ? timeFormat === "12-hour"
          ? "h:mm:ss a"
          : "HH:mm:ss"
        : "EEEE, MMMM d, yyyy";

    return localDateTime.toFormat(formatString);
  };

  return (
    <div className="app">
      <header className="header">
        <img
          src="/assets/atmospheric_logo.svg"
          alt="Atmospheric Logo"
          className="logo"
        />
      </header>
      <div className="search-row">
        <input
          type="text"
          value={city}
          onChange={(e) => {
            setCity(e.target.value);
            setSearchTriggered(false); // Reset search state
          }}
          placeholder="Enter a city..."
        />
        <button onClick={handleSearch}>Search</button>
        <button onClick={toggleUnitSystem}>
          {unitSystem === "imperial" ? "Metric" : "Imperial"}
        </button>
        <button onClick={toggleTimeFormat}>
          {timeFormat === "12-hour" ? "24hr" : "12hr"}
        </button>
      </div>
      <div className="time-row">
        {weatherData?.timezone !== undefined && (
          <p>
            Local time in {weatherData.name} is{" "}
            {getFormattedDateTime(weatherData.timezone, "time")} on{" "}
            {getFormattedDateTime(weatherData.timezone, "date")}.
          </p>
        )}
      </div>
      {error && searchTriggered && <p className="error">{error}</p>}
      {weatherData && searchTriggered && (
        <CurrentWeather
          weather={weatherData}
          unitSystem={unitSystem}
          sweetComment={getSweetMessage(
            weatherData.weather[0]?.description,
            isNightTime
          )}
        />
      )}
      {forecastData && searchTriggered && (
        <Forecast
          forecast={forecastData}
          unitSystem={unitSystem}
          timezoneOffset={weatherData?.timezone || 0}
        />
      )}
    </div>
  );
};

export default App;


















































