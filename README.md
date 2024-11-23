# WeatherApp Final Project 🌦️

## About the Project

The **WeatherApp** is a Python program that fetches weather data from the OpenWeather API. It shows you the current weather, a 5-day forecast, and even lets you look back at the weather history you’ve searched. This project is designed to showcase **design patterns** and includes tests to make sure everything works as expected.

---

## Features

1. **Current Weather**: See what’s happening right now in any city.
2. **5-Day Forecast**: Get a quick look at the highs, lows, and conditions for the next 5 days.
3. **Weather History**: Review past weather searches you've made.
4. **Local and City Time**: Shows both your local time and the time in the city you’re checking weather for.
5. **Future Plans**: 
   - Add a button to toggle between Fahrenheit/Celsius and mph/kph.
   - Add a 12-hour/24-hour clock toggle for the time display.

---

## Design Patterns I Used

I learned and used **5 design patterns** in this project:

1. **Factory Pattern**
   - This creates different weather objects, like current weather, forecasts, or history entries, in an organized way.

2. **Strategy Pattern**
   - Handles how time is calculated depending on whether it’s your local time or a city’s time (based on timezone offsets).

3. **Singleton Pattern**
   - Makes sure only one **HistoryManager** exists in the app so all history is managed consistently.

4. **Memento Pattern**
   - Saves and restores weather history entries (city, date, weather description, temperature).  
     - The **Originator** is each weather entry.  
     - The **Caretaker** is the **HistoryManager**, which saves, retrieves, and clears entries.  
     - The **Memento** is the saved history entry itself.  
   - This ensures the history feature is structured and easy to use.

5. **Template Method Pattern (Future Idea)**
   - This could process weather data into reusable formats for the current weather, forecasts, and history (something to add later!).

---

## Testing the App

I wrote **10 tests** to make sure everything works! These include:

1. **WeatherAPIClient Tests**:
   - Ensures the current weather and forecast API calls work.
   - Confirms the right weather icons show up for conditions like rain or snow.

2. **Time Strategy Tests**:
   - Verifies how time is calculated locally and for other cities.

3. **HistoryManager Tests**:
   - Tests saving, clearing, and handling duplicate weather history entries.

---

## CI/CD Pipeline (Fancy Automated Tests)

Every time I push code, GitHub Actions runs my tests to make sure I didn’t break anything. This is great because it catches problems fast.

**Badge**:  
![Python Tests](https://github.com/VU-cs5278/final-project-ElleLynn08/actions/workflows/python-tests.yml/badge.svg)

---

## How to Run It

### What You Need:
- Python 3.8+
- An OpenWeather API key

### Steps:
1. Clone this repo:
   ```bash
   git clone https://github.com/VU-cs5278/final-project-ElleLynn08.git
   cd final-project-ElleLynn08
   ```

2. Install what’s needed:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your API key:
   - Create a file called `.env` and add this line:
     ```bash
     API_KEY=your_api_key
     ```

4. Run the app:
   ```bash
   PYTHONPATH=. python src/main.py
   ```

5. Run the tests:
   ```bash
   PYTHONPATH=. python -m unittest discover tests
   ```

---

## Next Steps for the App

Here’s what I want to add in the future:

1. **Unit Conversion**: Add buttons to switch between Fahrenheit/Celsius and mph/kph.
2. **A Frontend**: Create a web interface to make the app even more user-friendly (I’m so excited about this part!).
3. **Weather Insights**: Compare current forecasts with last week’s weather.

---

## Contributing

This is a personal project for my course, but I’d love suggestions for improvements!

---

## License

This app is under the MIT License. See the LICENSE file for details.

---