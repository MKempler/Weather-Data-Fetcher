import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")

URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "imperial"
    }
    
    response = requests.get(URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}, check the city name or API key.")

    return response.json()
