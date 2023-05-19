import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time



engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("Good  Morning!")

    elif hour>=12 and hour<18:
        speak("Good  Afternoon")
        
    else:
        speak("Good  Evening")  

    speak("I am voice  assistant  sir ! Nice to meet you , Please  tell  me  how  may  i  help you.") 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1      
        audio = r.listen(source)

    try:
        print("Recognizing....")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query    

if __name__ == "__main__":
    wishme()

    while True:
      
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)   

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")   

        elif 'open email' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Public\\Music\\Sample Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Admins\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.8"
            os.startfile(codePath)
             
        elif 'open images' in query:
            image="C:\\Users\\Public\\Pictures\\Sample Pictures"
            os.startfile(image)


        else:
            webbrowser.open(query)
  
        time.sleep(5)
        print("do you have an another command for me? yes or no")
        speak("do  you  have  an  another  command  for  me?  yes  or  no")
        
        ans = takeCommand().lower()
        if 'no' in ans:
            print("GOOD  BYE  SIR... ")
            speak("good  bye  sir  ")
            exit()
        
        print("waiting for your command. please! give me a new command")
        speak(" waiting  for your  command . please!  give  me  a  new  command")
            
        
