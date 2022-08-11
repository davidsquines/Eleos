# import libraries

import speech_recognition as sr
import datetime

import pyttsx3
import datetime
import time
from functions.os_operations import open_spotify, open_vs_code, open_valorant
from functions.online_operations import play_on_youtube, google_query, get_weather_report

print('Loading your AI personal Assistant - Eleos')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Please Repeat that")
            return "None"
        return statement

speak("Loading Eleos")
wishMe()

if __name__=='__main__':
    while True:
        speak("How can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "nothing" in statement: 
            speak('Eleos is shutting down, Good Bye')
            print('Eleos is shutting down, Good Bye')
            break

        elif 'google search' in statement:
            speak('What would you like to search?')
            query = takeCommand().lower()
            google_query(query)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open spotify' in statement:
            open_spotify()
            time.sleep(5)
        
        elif 'open code editor' in statement:
            open_vs_code()
            time.sleep(5)

        elif 'play youtube video' in statement:
            speak("What video would you like to play")
            video = takeCommand().lower()
            play_on_youtube(video)
            time.sleep(5)

        elif 'play valorant' in statement:
            open_valorant()
            time.sleep(5)

        elif 'what is the weather' in statement:
            temp, feels_like = get_weather_report()
            speak(f"The current temperature is {temp}, but it feels like {feels_like}")
            speak("For your convenience, I am printing it on the screen")
            print(f"The current temperature is {temp}, but it feels like {feels_like}")
            time.sleep(5)

            



time.sleep(3)
