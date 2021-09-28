import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import playsound
from gtts import gTTS
import time
import random


print("Initializing Friday")
MASTER="Anubhav"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


#This function will take command from the microphone
r=sr.Recognizer()
def takeCommand(ask=False):
        with sr.Microphone() as source:
                if ask:
                   speak(ask)
                audio=r.listen(source)
                query = ''
                try:
                        query=r.recognize_google(audio)
                except sr.UnknownValueError:
                        speak("Sorry, I did not get that")
                except sr.RequestError:
                        speak("Sorry, my speech service is down")
                return query

#speak function will pronounce the string that is passed to it
def speak(audio_string):
  tts= gTTS(text=audio_string, lang= 'en')
  r= random.randint(1,1000000000)
  audio_file = 'audio-' + str(r) + '.mp3'
  tts.save(audio_file)
  playsound.playsound(audio_file)
  print(audio_string)
  os.remove(audio_file)

#speak("Anubhav is a rockstar")

speak("Initializing Friday")
#This function  will great you according to the cuurent time
def WishMe():
    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:
       speak("Good Morning" + MASTER) 

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

WishMe()



#Main program starts
def respond(query):
    

    #Logic for executing task as per query given

    if 'what is your name' in query.lower():
            speak("My name is Friday")
    if "creator" in query.lower():
            speak("My creator is Anubhav Banerjee")

    if 'wikipedia' in query.lower():
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 4)
            print(results)
            speak(results)

    elif 'open youtube' in query.lower():
            speak("Opening You Tube....")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            url="youtube.com"
            webbrowser.get(chrome_path).open(url)

    elif 'open stack overflow' in query.lower():
            speak("Opening stack overflow....")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            url="stackoverflow.com"
            webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
            print("playing Music...")
            songs_dir="C:\\Users\\HP\\Music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")

    elif 'photos' in query.lower():
            print("opening photos...")
            photo_dir="C:\\Users\\HP\\Pictures\\personal photos"
            os.startfile(photo_dir)
    
    elif 'search' in query.lower():
        speak("Okay, What do you want to search")
        search = takeCommand()
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url="https://google.com/search?q=" + search
        webbrowser.get(chrome_path).open(url)

    elif 'exit' in query.lower():
            exit()

time.sleep(1)
speak("Hi, How may I help you?")
while 1:  
  query=takeCommand()
  respond(query)
 