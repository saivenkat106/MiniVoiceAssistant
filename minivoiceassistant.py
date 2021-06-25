import pyttsx3 #pyttsx3 means python text to speech module
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
#engine.say("hello World")
#engine.runAndWait()
#print(voices)
voicespeed=180 #by default it will be 200wpm
engine.setProperty('rate',voicespeed)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak("This is venkat and welcome to my world")

def time():
    speak('current time is')
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

#time()

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak('current date is')
    speak(year)
    speak(month)
    speak(date)
#date()

def wishme():
    speak('welcome back')
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak('Good Morning')
    elif hour >=12 and hour<18:
        speak('Good Afternoon')
    elif hour>=18 and hour<=20:
        speak('Good Evening')
    else:
        speak('Good Night')
    speak('I am here for you and How can I help you')
#wishme()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak('Say that again ')
        return takeCommand()
    return query
#takeCommand()

def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("N160106@rguktn.ac.in","8885881315")
    server.sendmail("N160106@rguktn.ac.in",to,content)
    server.close()
def screenshot():
    img=pyautogui.screenshot()
    img.save("s.png")
    speak("screenshot is saved")
#screenshot()
def playsongs():
    songs_dir=r"C:\Users\saive\Music\SONGS"
    songs=os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir,songs[0]))
#playsongs()
def cpu():
    usage=str(psutil.cpu_percent())
    speak("Cpu is at"+usage)
def battery():
    battery=psutil.sensors_battery()
    speak("battery is at"+str(battery.percent))
#cpu()
#battery()
def joke():
    speak(pyjokes.get_joke())
#joke()

if __name__=="__main__":
    wishme()

    while True:
        query= takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentence=2)
            speak(result)
        elif "send mail" in query:
            try:
                speak("what should I say?")
                content=takeCommand()
                to="N160106@rguktn.ac.in"
                sendmail(to,content)
                speak("Email sent successfully")
            except:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath="C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            playsongs()
        elif "remember that" in query:
            speak("What should I remember")
            data=takeCommand()
            speak("you said me to remember"+data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("you said me to remember that"+remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done")
        elif "cpu" in query:
            cpu()
        elif "battery" in query:
            battery()
        elif "joke" in query:
            joke()
            
            
            





    
