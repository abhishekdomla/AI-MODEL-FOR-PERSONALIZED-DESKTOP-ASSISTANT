from doctest import master
from inspect import FrameInfo
import time
import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import sys
import ctypes
import win32com.client as wincl
from ecapture import ecapture as ec
import pyaudio
import smtplib
import pyjokes
import subprocess
import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
import json


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# speaking

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# greeting
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        speak("thank you for activating me , how may I help you")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        speak("thank you for activating me , how may I help you")

    else:
        speak("Good Evening!")  
        speak("thank you for activating me , how may I help you")
# command
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in , mr-IN , hi-IN ')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def basicomand():
    # It continuously listens for user input until a valid query is fetched
    while True:
        try:
            # It takes microphone input from the user
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 0.5
                audio = r.listen(source)

            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            
            # If the query is successfully recognized, return it
            return query
            
        except Exception as e:
            # If an error occurs, print the error and continue listening
            print(e)
            print("Please speak again...")
            speak('Please speak again...')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rohan.d.chikane.2003@gmail.com', '')
    server.sendmail('abhishekdomala2000@gmail.com', to, content)
    server.close()

def terminate():
    sys.exit()

###### NEWS ####### require a note


# ===========================
# -------------------

# if __name__ == '__main__':
#     while True:
#         try:
#             # Taking input from the user
#             user_input = input("Enter something: ")
#             if "english" in user_input:
#                 english() 
#             else:
#                 break
#         except Exception as e:
#             # Handle the exception (e.g., invalid input)
#             print("Error:", e)
#             print("Please try again.")