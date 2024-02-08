import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from AppOpener import open


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def process_voice_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    return ""

def openApp(app):
    open(app,match_closest=True)
    
def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    print("Hello")
    command = process_voice_command()    
    print(command.lower())
    if command.lower()== "open google":
        webbrowser.open("https://www.google.com")
    elif command.lower()=="open youtube":
        webbrowser.open("https://www.youtube.com")
    elif command.lower()== "open wikipedia":
        webbrowser.open("https://www.wikipedia.org")
    elif command.lower() == "open gmail":
        webbrowser.open("https://mail.google.com")
    elif command.lower() == "open google drive":
        webbrowser.open("https://drive.google.com")
    elif command.lower() =="open onedrive":
        webbrowser.open("https://onedrive.live.com")
    elif command.lower() == "open google calendar":
        webbrowser.open("https://calendar.google.com")
    elif command.lower() == "open google maps":
        webbrowser.open("https://maps.google.com")
    elif command.lower() == "open google news":
        webbrowser.open("https://news.google.com")
   
    elif command.lower() == "open chrome":
        openApp("chrome")
    elif command.lower() == "open brave":
        openApp("brave")
    elif command.lower() == "open clock":
        openApp("clock")
    elif command.lower() == "open chrome":
        openApp("chrome")
    elif command.lower() == "open telegram":
        openApp("telegram")
    elif command.lower() == "open whatsapp":
        openApp("whatsapp")
    elif command.lower() == "open setting":
        openApp("setting")



    elif command.lower() == "goodbye":
        speak("Goodbye!")


    else:
        speak("Sorry, I didn't understand that.")
