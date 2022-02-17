from sqlite3 import Date
import requests
import os
from PIL import Image
import pyttsx3
import random
import scipy 
import matplotlib.pyplot as plt
import datetime
import cartopy.crs as ccrs 
import matplotlib.pyplot as plt


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

Api_Key = "VELOb8LM3sRgafwWiNpROrIjFGYoeHK0JCnsOqcv"

def NasaNews(Date):

    

    speak("Extracting data From Nasa")


    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date':str(Date)}

    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "C:\\Users\\91930\\Desktop\\python\\jerry\\" + str(FileName)

    Path_2 = "C:\\Users\\91930\\Desktop\\python\\jerry\\files\\" + str(FileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    speak(f"Title : {Title}")
    speak(f"According To nasa : {Info}")

def MarsImage():

    name = 'curiosity'

    date = '2020-12-3'

    Api_ = str(Api_Key)

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"

    r = requests.get(url)

    Data = r.json()

    Photos = Data['photos'][:20]

    try:

        for index , photo in enumerate(Photos):

            camera = photo['camera']

            rover = photo['rover']

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img,'wb') as file:
                file.write(p.content)

            Path_1 = "C:\\Users\\91930\\Desktop\\python\\jerry\\" + str(img)

            Path_2 = "C:\\Users\\91930\\Desktop\\python\\jerry\\files\\mars\\" + str(img)

            os.rename(Path_1,Path_2)

            os.startfile(Path_2)

            speak(f"this image was capturesd with : {full_camera_name}")

            speak(f"this image was captured on : {date_of_photo}")

    except:
        speak("something wrong")

def Astro(start_date,end_date):

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"

    r = requests.get(url)

    Data = r.json()

    Total_Astro = Data['element_count']

    neo = Data['near_earth_objects']

    speak(f"Total Astroid Between {start_date} and {end_date} is: {Total_Astro}")

    speak("Extract data of those Astroids Are listed Below")

    for body in neo[start_date]:

        id = body['id']

        name = body['name']

        absolute = body['absolute_magnitude_h']

        print(id,name,absolute)

def Spacebodies(body):

    url = "https://api.le-systeme-solaire.net/rest/bodies/"

    r = requests.get(url)

    Data = r.json()

    bodies = Data['bodies']

    Number = len(bodies)

    #for bodyyy in bodies:
        #print(bodyyy['id'],end=',')

    url_2 = "https://api.le-systeme-solaire.net/rest/bodies/" + str(body)

    rrr = requests.get(url_2)

    data_2 = rrr.json()

    mass = data_2['mass']['massValue']

    volume = data_2['vol']['volValue']

    density = data_2['density']

    gravity = data_2['gravity']

    escape = data_2['escape']

    speak(f"Number of bodies in solar system : {Number} .")
    speak(f"mass of {body} is {mass} .")
    speak(f"Gravity of {body} is {gravity} .")
    speak(f"Escape velocity of {body} is {escape} .")
    speak(f"density of {body} is {density} .")
    speak(f"Volume of {body} is {volume} .")

def Summary(Boby):

    list__ = ('1','2','3','4')

    value = random.choice(list__)

    path = "C:\\Users\\91930\\Desktop\\python\\jerry\\files\\space\\" + str(value) + ".jpg"

    os.startfile(path)

    name = str(Boby)

    url = 'https://hubblesite.org/api/v3/glossary/' + str(name)

    r = requests.get(url)

    Data = r.json()

    if len(Data) != 0:

        retur = Data['definition']

        speak(f"According to Nasa: {retur}")

def IssTracker():

    url = "http://api.open-notify.org/iss-now.json"

    r = requests.get(url)

    Data = r.json()

    dt = Data['timestamp']

    lat = Data['iss_position']['latitude']

    lon = Data['iss_position']['longitude']

    speak(f"Time And Date : {dt}")
    speak(f"Latitude : {lat}")
    speak(f"Longitude : {lon}")

    plt.figure(figsize=(10,8))

    ax = plt.axes(projection = ccrs.PlateCarree())

    ax.stock_img()

    plt.scatter(float(lon),float(lat),color = 'blue' , marker= 'o')

    plt.show()
IssTracker()















