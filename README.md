# Weather Application using Tkinter

This Python application fetches and displays current weather information for a specified city using the OpenWeatherMap API. It provides a simple user interface built with Tkinter.

## Features

- **City Input:** Enter the name of a city to fetch weather data.
- **Unit Selection:** Choose between Celsius (metric) and Fahrenheit (imperial) units.
- **Display:** Shows current temperature, atmospheric pressure, humidity, and weather description.
- **Error Handling:** Alerts users for invalid inputs or if the city is not found.

**Install dependencies:**
  Ensure you have Python installed. Install required Python packages using pip:
   ```bash
   pip install tkinter requests
   ```

**API Key Setup:**
- Obtain an API key from [OpenWeatherMap](https://openweathermap.org/).
- Replace `API_KEY` in the 'code' with your API key.

## Usage
**Using the Application:**

   - Enter a city name in the provided entry field.
   - Select either `metric` (Celsius) or `imperial` (Fahrenheit) for temperature units.
   - Click on "Get Weather" to fetch and display weather data.
   - Click "Back" to return to the main input screen.
