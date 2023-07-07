# Weather App

The Weather App is a Python-based desktop application that provides real-time weather data by making API calls to OpenWeatherMap. It allows users to fetch and display weather information for a specific location, including current temperature, humidity, and weather description. The app also supports location-based forecasts, giving users insights into the weather conditions for the upcoming days.

## Features

- Fetch real-time weather data from OpenWeatherMap API
- Display current temperature, humidity, and weather description
- Support for location-based forecasts
- User-friendly graphical user interface
- Seamless data retrieval and display

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/weather-app.git
Install the required dependencies:

shell
Copy code
pip install -r requirements.txt
Usage
Run the application:

shell
Copy code
python main.py
Enter the name of a city and optionally the state and country to fetch the weather data.

The application will display the current weather information for the specified location.

Dependencies
requests: Library for making HTTP requests
python-dotenv: Library for loading environment variables from a .env file
tkinter: Standard GUI library for Python
API Key
The Weather App requires an API key from OpenWeatherMap to fetch weather data. Make sure to sign up on the OpenWeatherMap website to obtain an API key. Once you have the API key, create a .env file in the project's root directory and add the following line, replacing YOUR_API_KEY with your actual API key:

makefile
Copy code
OPEN_WEATHER_MAP_API_KEY=YOUR_API_KEY
Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. See CONTRIBUTING.md for more details.

License
This project is licensed under the MIT License.
