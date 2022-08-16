from tkinter import E
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Della Maam. Please tell me how can I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print(" YES! Listening...")
        r.pause_threshold =1 #for taking a break
        audio=r.listen(source)
    try:
        print(" I am working on it...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could you repeat that please....")
        return "None"
    return query
if __name__== "__main__":
    wishMe()
    while True:
        query=takeCommand().lower() 
        #logic for executing task based on query

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Wikipedia states that..")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Just a second mam")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.org")
        elif 'play music' in query:
            music_dir='C:\\Users\\ASUS\\Music\\favorite'
            song=os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f" Mam The time is{strTime}")
        elif 'open code ' in query:
            path="C:\\Users\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'you are awesome' or 'nice work' in query:
            speak("That is my job mam")
        elif 'Who made you?' in query:
            speak("I was created by Miss SWATI")
        elif 'quit' in query:
            quit()
        else:
            speak("Sorry this is out of range but I would love to help you again.")
