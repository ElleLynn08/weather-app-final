import axios from "axios";

const BASE_URL = "http://localhost:5000"; // Your Python backend URL

export const getCurrentWeather = (city) => axios.get(`${BASE_URL}/weather/current?city=${city}`);
export const getForecast = (city) => axios.get(`${BASE_URL}/weather/forecast?city=${city}`);
export const getHistory = () => axios.get(`${BASE_URL}/weather/history`);
