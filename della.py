
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random


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

    speak("I am Della, Maam. Please tell me how can I help you")   


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


        ### **** ---- WEB ACTIVITIS -----*****

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
        elif 'open code ' in query:
            path="C:\\Users\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            
           
            ### ----** Date, Time and Day**---- 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(strTime)
            speak(f"boss, the Time is {strTime}")

        elif "the date" in query :
            strDate = datetime.date.today().strftime("%B %d, %y")
            print(strDate)
            speak(f'boss, the Date is {strDate}')

        elif "the day" in query :
            strDay = datetime.datetime.now().strftime("%A")
            print(strDay)
            speak(f'boss, the Day is {strDay}')
        
                     
        
        
        #### ----**** DELLA'S ACTIVITY *****---- 


        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f" Mam The time is{strTime}")

        elif 'you are awesome' in query or 'nice work' in query:
            speak("That is my job mam")

        elif 'who made you' in query or 'designed you' in query:
            l = ["i started as an idea, then my maam, swati helped bring me to the life",'who calls her mother by name',"A very gorgeos lady with the sharp mind, and a kind hearted swati hiranwar",'swati hiranwar is my boss']
            speak(random.choice(l))

        elif "what are you doing" in query:
            l = ["trying to be better,  ma'am", "thinking, what are you thinking, maam ",'nothing much,  boss']  
            speak(random.choice(l))

        elif 'your birthday' in query :
            l = ['i was designed on,  16th of the july in the evening',"16 july was that auspicious day for me",'16 july  was the day when my boss  converted her idea into reality '] 
            speak(random.choice(l))

        elif "how are you" in query or "how is you" in query :
            l = ['i am great!, thank you for asking, boss', "woundring how is you", "thank for asking, i'm doing ok. a lot is going on in this world today. i hope you are taking care of yurself",'im fine. your are very kind to ask, specially in this tempestupus time','i am good, thank you for asking . i hope your are doing well too. if i can help with anything, just ask ']
            speak(random.choice(l))

        elif "ok bye" in query or "see you later" in query :
            l = ['do let me know,   when you need somthing', 'ok sir,  call me whenever you need somthing', 'happy to serve you','always remember im just a call away,  boss']
            speak(random.choice(l))
            quit()
