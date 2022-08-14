import pywhatkit as kit
import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API = os.getenv('OPEN_WEATHER_API_KEY')
LAT = os.getenv('LAT')
LONG = os.getenv('LONG')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def play_on_youtube(video):
    kit.playonyt(video)

def google_query(query):
    kit.search(query)

def get_weather_report():
    res = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LONG}&exclude=minutely,hourly,daily,alerts&appid={WEATHER_API}&units=imperial").json()
    temp = res["current"]["temp"]
    feels_like = res["current"]["feels_like"]
    return temp, feels_like

def get_news_report(category):
    news = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}").json()
    articles = res['articles']
    for article in articles:
        newsArticle = {
            'title' : article["title"],
            'description' : article['description'],
            'url' : article['url']
        }
        news.append(newsArticle)
    return news[:5]

    
