# import libraries

import speech_recognition as sr

r = sr.Recognizer()

# get default microphone
with sr.Microphone() as source:
    # listens to a command, using awd

    while True:
        audio = r.listen(source)

        text = r.recognize_google(audio)

        print(text)