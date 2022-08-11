import pywhatkit as kit
import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API = os.getenv('OPEN_WEATHER_API_KEY')
LAT = os.getenv('LAT')
LONG = os.getenv('LONG')

def play_on_youtube(video):
    kit.playonyt(video)

def google_query(query):
    kit.search(query)

def get_weather_report():
    res = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LONG}&exclude=minutely,hourly,daily,alerts&appid={WEATHER_API}&units=imperial").json()
    temp = res["current"]["temp"]
    feels_like = res["current"]["feels_like"]
    return temp, feels_like