from click import command
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyjokes
import pyaudio
import requests
import smtplib
import webbrowser
import time
import instaloader
import wikipedia
import PyPDF2
import operator
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
import pywhatkit as kit
import sys  
import cv2
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
from pytube import YouTube
from playsound import playsound
import keyboard
from googletrans import Translator
from keyboard import press
from keyboard import press_and_release
from keyboard import write 
from time import sleep
import wolframalpha
from nasa import Api_Key



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 120)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=100, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Lucky Said: {query}")

    except Exception as e:
        # speak("Say that again please...")
        return 'none'
    query = query.lower()
    return query

# To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hello sir I am Jerry, tell me how can i help you")

# for news updates
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=Api_key

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

# for chrome automation
def ChromeAuto():
    speak("tell me the command")
    command = takecommand()

#hindi class
def TakeHindi():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio,language='hi')
            print(f"You Said : {query}")

        except:
            return "none"

        return query.lower()

#translator
def Tran():
    speak("Tell Me The Line!")
    line = TakeHindi()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak(Text)

#youtube auto
def YoutubeAuto():
    speak("Whats Your Command ?")
    comm = takecommand()

    if 'pause' in comm:
        keyboard.press('space bar')

    elif 'restart' in comm:
        keyboard.press('0')

    elif 'mute' in comm:
        keyboard.press('m')

    elif 'skip' in comm:
        keyboard.press('l')

    elif 'back' in comm:
        keyboard.press('j')

    elif 'full screen' in comm:
        keyboard.press('f')

    elif 'film mode' in comm:
        keyboard.press('t')


    elif 'my channel' in query:

        web.open("place your channel link")

    else:
        speak("No Command Found!")

    speak("Done Sir")

#open apps
def OpenApps():
    speak("Ok Sir , Wait A Second!")
        
    if 'code' in query:
        os.startfile("C:\\Users\\91930\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        #give your path here

    elif 'telegram' in query:
        os.startfile("C:\\Users\\91930\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        #give your path here

    elif 'chrome' in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        #give your path here

    elif 'Whatsapp' in query:
        os.startfile("C:\\Users\\91930\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
        #give your path here

    elif 'facebook' in query:
        webbrowser.open('https://www.facebook.com/')
        #give your path here

    elif 'instagram' in query:
        webbrowser.open('https://www.instagram.com/')

    elif 'open drive' in query:
        webbrowser.open('https://drive.google.com')

    elif 'map' in query:
        webbrowser.open('https://www.google.com/maps/')

    elif 'youtube' in query:
        webbrowser.open('https://www.youtube.com')
        speak("Your Command Has Been Completed Sir!")

#close apps
def CloseAPPS():
    speak("Ok Sir , Wait A second!")

    if 'youtube' in query:
        os.system("TASKKILL /F /im Chrome.exe")

    elif 'chrome' in query:
        os.system("TASKKILL /f /im Chrome.exe")

    elif 'telegram' in query:
        os.system("TASKKILL /F /im Telegram.exe")

    elif 'code' in query:
        os.system("TASKKILL /F /im code.exe")

    elif 'instagram' in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif 'map' in query:
        os.system("TASKKILL /F /im chrome.exe")

            
    speak("Your Command Has Been Succesfully Completed!")

#temprature
def Temp():
    search = "temperature in Delhi"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_="BNeawe").text
    speak(f"The Temperature Outside Is {temperature}")

    speak("Do I Have To Tell You Another Place Temperature ?")
    next = takecommand()

    if 'yes' in next:
        speak("Tell Me The Name Of tHE Place ")
        name = takecommand()
        search = f"temperature in {name}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_="BNeawe").text
        speak(f"The Temperature in {name} is {temperature}")

#coronavirus track
def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)
    import bs4
    soups = bs4.BeautifulSoup(result.text,'lxml')
    corona = soups.find_all('div',class_ = 'maincounter-number')
    Data = []
    for case in corona:
        span = case.find('span')
        Data.append(span.string)
    cases , Death , recovored = Data
    speak(f"Cases : {cases}")
    speak(f"Deaths : {Death}")
    speak(f"Recovered : {recovored}")

#dATE cONVERTER
def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)



    Term = str(query)

    Term = Term.replace("jerry","")
    Term = Term.replace("in","")
    Term = Term.replace("what is the","")
    Term = Term.replace("what is the","")
    Term = Term.replace("tempature","")

    temp_query = str(Term)

    if "outside" in temp_query:

        var1 = "Temprature in prayegraj"

        answer = Wolfram(var1)

        speak(f"{var1} is {answer} .")

    else:

        var2 = "Temprature in " + temp_query

        answ = Wolfram(var2)

        speak(f"{var2} is {answ}")



if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # Logic building for tasks

        if "open notepad" in query:
            npath = 'C:\\Windows\\System32\\notepad.exe'
            #give your path here
            os.startfile(npath)
            speak("opening")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\91930\\3D Objects\\New folder'
            #give your path here
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[128]))
            speak("playing music")

        # To Close any application
        elif 'close notepad' in query:
            speak("okay sir, closing")
            os.system("taskkill /f /im notepad.exe")

        # To find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 10")

        elif "restart the system" in query:
            os.system("shutdown /r /t 10")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(10)
            pyautogui.keyUp("alt")

        elif "tell me the news" in query:
            speak("please wait sir, while fetching the news for you")
            news()

        # to find my location using IPaddress
        elif "where i am" in query or "where we are" in query:
            speak('wait sir, let me check')
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in{city} city of {country}")
            except Exception as e:
                speak("sorry sir,due to network issue i amnot able to find where we are.")
                pass

        # to take screenshot
        elif "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()           
            img.save(f"{name}.png")
            speak("i am done sir, screenshot is taken in our main folder")
         
        #astroid near earth
        elif "tell me the asteroid near earth" in query:
            from nasa import Astro
            speak("tell me the starting date...")
            start = input('enter the start date:')
            speak("tell me the end date..")
            end = input('enter the end date here:')
            Astro(start,end)
        
        #solar bodies near earth
        elif "tell me the solar body" in query:
            from nasa import Spacebodies
            speak("tell me the body name")
            bod = input("Enter the body name: ") 
            body = bod.replace(" ","")
            body = body.replace(" ","")
            Body = str(body)
            Spacebodies(body=Body)
        
        # about jerry

        if "hello" in query or "hey" in query:
            speak("hello sir, may I help you with something")

        elif "how are you" in query:
            speak("I am fine sir, what about you")

        elif "also good" in query:
            speak("that's great to hear from you")

        elif "thank you" in query:
            speak("it's my pleasure sir")

        # to hide files and folder
        elif "hide all files" in query or "hide this folder" in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all files are now hidden")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir,all the files are now visible")

            elif "leave it" in condition:
                speak("ok sir")

        # how to do mode
        elif "activate how to do mod" in query:
            speak("how to do mode is activated")
            while True:
                speak("please tell me what do you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir,how to do mode is activated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)  # pip install pywikihow
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry, not able to find")

        # to know battery percentage
        elif "how much power " in query or "battery" in query:
            import psutil

            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage >= 75:
                speak("we have enough power, no need to charge")
            elif percentage >= 40 and percentage <= 75:
                speak("we should connect our system to the charging point")
            elif percentage >= 15 and percentage <= 30:
                speak("we don't have enough power,please connect to the charger")
            elif percentage <= 15:
                speak("we ahve very low power , please connect to the charger")

        # to play video and audio on yt
        elif "play songs on youtube" in query:
            try:
                speak("tell me the song name")
                name = input("please Enter the song name here")
                kit.playonyt(name)
            except Exception as e:
                speak("sorry sir i am unable to search")

        # SHUT UP
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        #web search
        if "open google" in query:
            speak("what should i search")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("opening")
        
        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        # open camera
        if "open camera" in query:
            import urllib.request
            import cv2 # pip install opencv-python
            import numpy as np # pip install numpy
            import time
            URL = "http://25.220.18.57:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break;

            cv2.destroyAllWindows

        # set alarm
        elif "set alarm" in query:
            speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time To Wake Up Sir!")
                    playsound('05 Main Tera Boyfriend - Raabta (Arijit Singh) 190Kbps.mp3')
                    speak("Alarm Closed!")

                elif now>time:
                    break

        # ip address
        elif "ip address" in query:
            from requests import get
            ip = get("https://api.ipify.org").text
            speak(f"your IP address is {ip}")

        # to send massage 

        elif "send a message" in query:
            speak("sir, what should i say")
            msz = takecommand()

            from twilio.rest import Client

            account_sid = 'AC9c9aa8edcfffdff29b3ddf320f104884'
            auth_token = '1fd8c3382456e2a5dc9a81524cbb1363'

            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body= msz,
                    from_='+16076009288',
                    to='+919305486556'
                )

            print(message.sid)
            speak("sir, message has been sent")

        # to make call
        elif "make a call" in query:

            speak("sir, what should i say")
            msz = takecommand()

            from twilio.rest import Client

            account_sid = 'AC9c9aa8edcfffdff29b3ddf320f104884'
            auth_token = '1fd8c3382456e2a5dc9a81524cbb1363'

            client = Client(account_sid, auth_token)

            message = client.calls \
                .create(
                    twiml= '<Response><say>this is second testing message..</Say></Response>',
                    from_='+16076009288',
                    to='+919305486556'
                )

            print(message.sid)

        # to visit mars
        elif "mars images" in query:
            from nasa import MarsImage
            MarsImage()

        # Reply

        if "bye" in query:
            from database.chatbot.Chatbot import Chatterbot
            reply = Chatterbot(query)
            speak(reply)
            break

        elif "exit" in query:
            from database.chatbot.Chatbot import Chatterbot
            reply = Chatterbot(query)
            speak(reply)
            break

        elif 'go' in query:
            from database.chatbot.Chatbot import Chatterbot
            reply = Chatterbot(query)
            speak(reply)
            break

        # make jerry memorious
        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jerry","")
            speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("You Tell Me That" + remeber.read())

        # to download video

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            speak("Video Downloaded")

        # repatable jerry
        elif 'repeat my word' in query:
            speak("Speak Sir!")
            jj = takecommand()
            speak(f"You Said : {jj}")

        #automate
        elif 'chrome automation' in query:
            ChromeAuto()
        
        #keyboard automation
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'volume up' in query:
            keyboard.press('Fn + F8')

        elif 'volume down' in query:
            keyboard.press('fn + f7')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query: 
            keyboard.press_and_release('ctrl +h')

        elif 'home screen' in query:

            keyboard.press_and_release('windows + m')

        elif 'minimise the window' in query:

            keyboard.press_and_release('windows + m')

        elif 'show start' in query:

            keyboard.press('windows')

        elif 'open setting' in query:

            keyboard.press_and_release('windows + i')

        elif 'open search' in query:

            keyboard.press_and_release('windows + s')

        elif 'screen shot' in query:

            keyboard.press_and_release('windows + SHIFT + s')

        elif 'restore windows' in  query:

            keyboard.press_and_release('Windows + Shift + M')

        elif 'increase' in query:

            keyboard.press_and_release('SHIFT + .')

        elif 'decrease' in query:

            keyboard.press_and_release('SHIFT + ,')

        elif 'previous' in query:

           keyboard.press_and_release('SHIFT + p')

        elif 'next' in query:

           keyboard.press_and_release('SHIFT + n')
    
        elif 'search' in query:
           
           press(x=667, y=146)

           speak("What To Search Sir ?")

           search = takecommand()

           write(search)

           sleep(0.8)

           keyboard.press('enter')

        elif 'mute' in query:

           keyboard.press('m')

        elif 'unmute' in query:

           keyboard.press('m')

        elif 'start the video' in query:
            keyboard.press('space bar')

        #website automation
        elif 'website' in query:
            speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launched!")

        elif 'launch' in query:
            speak("Tell Me The Name Of The Website!")
            name = input("enter the website name: ")
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")

        # open apps
        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open map' in query:
            OpenApps()

        elif 'open drive' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open whatsapp' in query:
            OpenApps()

        # close apps
        elif 'close chrome' in query:
            CloseAPPS()

        elif 'Code' in query:
            CloseAPPS()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'close map' in query:
            CloseAPPS()

        #translator
        elif 'translator' in query:
            Tran()
        #temprature
        elif 'temperature' in query:
            Temp()
        #corona track
        elif 'coronavirus cases' in query:

            from jerry import CoronaVirus

            speak("Which Country's Information ?")

            cccc = takecommand()

            CoronaVirus(cccc)

        elif 'track space station' in query:

            from nasa import IssTracker

            IssTracker()

        #automate whatsapp
        elif 'whatsapp message' in query:
            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            speak(f"Whats The Message For {Name}")
            MSG = takecommand()
            from Automation import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automation import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jerry ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            speak("With Whom ?")
            name = takecommand()
            from Automation import WhatsappChat
            WhatsappChat(name)

        #space autoations
        elif 'space news' in query:

            speak("Tell Me The Date For News Extracting Process .")

            Date = input("Enter the date")

            Value = (Date)

            from nasa import NasaNews

            NasaNews(Value)
      
        #online class automate
        elif 'online' in query:

            from Automation import OnlinClass

            speak("Tell Me The Name Of The Class .")

            Class = takecommand()

            OnlinClass(Class)
