from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from os import startfile
import os
from time import sleep
import webbrowser as wb

def WhatsappMsg(name,message):
     
    wb.open("https://web.whatsapp.com//")

    sleep(10)

    click(x=195, y=115)

    sleep(1)

    write(name)

    sleep(0.5)

    click(x=188, y=249)

    sleep(0.5)

    click(x=571, y=690)

    sleep(0.5)

    write(message)

    press('enter')




def WhatsappCall(name):

    startfile("https://web.whatsapp.com/")

    sleep(10)

    click(x=195, y=115)

    sleep(1)

    write(name)

    sleep(1)

    click(x=188, y=249)

    sleep(1)

    click(x=571, y=690)

    sleep(1)

    click(x=1198, y=63)

WhatsappCall("Chaccha")


def WhatsappChat(name):

    startfile("C:\\Users\\91930\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=195, y=115)

    sleep(1)

    write(name)

    sleep(1)

    click(x=188, y=249)

    sleep(1)

    click(x=571, y=690)

    sleep(1)

def OnlinClass(Subject):

    Speak("Joining The Class Sir .")

    if 'science' in Subject:

        from DataBase.OnlineClasses.Links import Science

        Link = Science()

        web.open(Link)

        sleep(10)

        click(x=412, y=571)

        sleep(1)

        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'mathematics' in Subject:

        from DataBase.OnlineClasses.Links import Maths

        Link = Maths()

        web.open(Link)

        sleep(10)

        click(x=412, y=571)

        sleep(1)

        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'social' in Subject:

        from DataBase.OnlineClasses.Links import sst

        Link = sst()

        web.open(Link)

        sleep(10)

        click(x=412, y=571)

        sleep(1)

        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'hindi' in Subject:

        from DataBase.OnlineClasses.Links import Hindi

        Link = Hindi()

        web.open(Link)

        sleep(10)

        click(x=412, y=571)

        sleep(1)

        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'english' in Subject:

        from DataBase.OnlineClasses.Links import English
