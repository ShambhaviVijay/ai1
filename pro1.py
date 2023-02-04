import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
#import pyaudio

import os

engin=pyttsx3.init('sapi5')
voices=engin.getProperty('voices')
engin.setProperty('voices',voices[0].id)

def speak(audio):
        engin.say(audio)
        engin.runAndWait()

def wish():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
                speak("good morning")
        elif hour>=12 and hour<18:
                speak ("good afternoon")
        else:
                speak("good night")
        speak (" have a good day ahead.")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__=="__main__":
        speak("hello i am jarvis coded by trisha on 26th march 2022")
        wish()
        query=takeCommand().lower()
#logic to execute tasks based on query

        if 'wikipedia' in query:
                speak('Searching wikipedia...')
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences =4)
                speak("according to wikipedia")
                print(results)
                speak(results)
        elif 'open youtube' in query:
                webbrowser.open("youtube.com")
        elif 'open google' in query:
                webbrowser.open("google.com")
                
        
        #here you can visit github also to open github
        elif 'open github' in query:
                webbrowser.open("github.com")
       

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            music_dir = 'D:\\s'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
                
        
        
