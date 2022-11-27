import time
import pyautogui as pg
from random import randint as rd
from datetime import datetime as dt


import pyttsx3
from pytube import YouTube as yt

import pandas as pd
import numpy as np
import re

#lol dare
import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import interact_manual
import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px




now = dt.now()

hk= dt(now.year, now.month, now.day, 13, 00)
time_remaining = hk - now


def say(text):
    engine = pyttsx3.init()
    text = [text]
    for i in text:
        engine.say(i)
        engine.runAndWait()

def randomList(itens):
    here = []
    here = itens
    if here is not None:
        return here[rd(0, len(itens)-1)]

lofis = ["https://youtu.be/jhvUqV3qeC0", "https://youtu.be/wtg7AetxuWo",
         "https://youtu.be/uUR4020kmrs", "https://youtu.be/jrTMMG0zJyI",
         "https://youtu.be/6me17gGZYRg"]


adventure_musics = ["https://youtu.be/B7xai5u_tnk",
                    "https://youtu.be/cMg8KaMdDYo",
                    "https://youtu.be/j-2DGYNXRx0",
                    "https://youtu.be/wKRL7vkWMoc",
                    "https://youtu.be/p7ZsBPK656s",
                    "https://youtu.be/yJg-Y5byMMw",
                    "https://youtu.be/fiore9Z5iUg"]


adventure_music = randomList(adventure_musics)

lofi = randomList(lofis)



eletronic_musics =["https://youtu.be/vPUp5pzh8Mc", "https://youtu.be/fiore9Z5iUg"]
eletronic_music = randomList(eletronic_musics)

relaxing_musics = ["https://youtu.be/FaX64o71vGQ"]
relaxing_music = randomList(relaxing_musics)

def checkBool(check_item, list_of_itens):
    Check = False
    for i in range(len(list_of_itens)):
        if check_item == list_of_itens[i]:
            return True
        else:
            Check = False
    return Check

def newTab(url, _interval = 0.075):
    pg.hotkey("ctrlleft","t")
    time.sleep(1)
    pg.typewrite(url, interval = _interval)
    pg.press("enter")

def openGoogle(times = 5):
    #google
    pg.press("winleft")
    pg.typewrite("Google", interval = 0.25)
    pg.press("enter")
    time.sleep(times)
    pg.click(650, 550,duration =1)
    time.sleep(1)

def winR (text):
    pg.hotkey("winleft","r")
    if text is not None:
        pg.typewrite(text)
        pg.press("enter")

def openLeagueOfLegends(period = 45):
    #entrar no lolzinho 
    usuary = "roema123"
    password = "Alex21032001!"


    #abrir lolzinho
    openProgram("League")

    #logar
    time.sleep(period)
    pg.typewrite(usuary, interval = 0.05)
    pg.press("tab")
    pg.typewrite(password, interval = 0.05)
    pg.press("enter")

def openProgram(name):
    pg.press("winleft")
    pg.typewrite(name, interval = 0.25)
    pg.press("enter")
    time.sleep(1)

def Map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def Flux(intesity):
    openProgram("f.lux")
    pg.click(1125,1001, duration = 1)
    pg.moveTo(741,720, duration = 1)
    pg.drag((Map(intesity, 0, 100, 0, 376), 0), duration = 1)

def Sound(intensity, fade = 1):
    pg.click(1176,1002, duration = 1)
    pg.click(1172,879, duration = 0.5)
    pg.moveTo(1172,879, duration = 1)
    pg.drag(0, Map(intensity, 0, 100, 0, -111), duration = fade)

def openfile(x):
    winR(x)

def setup(name, times = 45):
    if name == ("download"):
        def download( link ):
            youtubeObjc = yt(link)
            try:
                youtubeObjc.streams.first().download()
            except:
                print("something wrong ocurred")
            print("Sucess")
        download(str(input("YOUTUBE URL: ")))
        
    if checkBool(name, ["cursos", "curso"]):
        openGoogle()
        newTab("https://www.udemy.com/")
        newTab("https://humanosforadacurva.com/courses")
        newTab("https://membros.nucleoexpert.com/")
        time.sleep(3)
        pg.click(950,700,duration = 1)
        newTab("https://youtu.be/vPUp5pzh8Mc")
        
    if checkBool(name, ["games", "gaming", "lol", "game"]):
        openProgram("f.lux")
        openLeagueOfLegends(period = 60)
        Sound(12)
        openGoogle()
        newTab(eletronic_music)
        newTab("https://www.metasrc.com/5v5/champion/swain/support")
        newTab("https://web.whatsapp.com/")
        
    if name == "lofi" or name == "night glory" or name == "night":
        Flux(20)
        openGoogle()
        newTab(lofi)
        newTab("https://keep.google.com/")
        newTab("https://calendar.google.com/")
        newTab("https://open.spotify.com/")

    if checkBool(name, ["chat", "chatting", "friends"]):
        say("Oh Right! I'm opening the chats for you. Whatsapp. Instagram an so on. Take a breath. enjoy.")
        openProgram("f.lux")
        openGoogle()
        newTab("https://instagram.com")
        newTab("https://web.whatsapp.com")
        newTab("https://facebook.com/")
        newTab("https://web.telegram.org/k/")
        newTab("https://photos.google.com")

    if checkBool(name,["draw", "drawing"]):
        openProgram("f.lux")
        openGoogle()
        newTab("https://pintelest.com")
        newTab("https://youtube.com")
        newTab(adventure_music)
    if name == "python":
        say("Congrats, I'm opening Python for you now! Enjoy this litle moment. Take a breath!")
        openProgram("cmd")
        time.sleep(2)
        pg.write("jupyter notebook", interval = 0.1)
        pg.press("enter")
        time.sleep(12)
        newTab("https://www.udemy.com/course/machine-learning-data-science-python/learn/lecture/26035392")
        newTab(adventure_music)
    if checkBool(name, ["strategy", "strateg", "calendar and keep", "google keep"]):
        openGoogle()
        newTab(lofi)
        newTab("https://keep.google.com/")
        newTab("https://calendar.google.com/")
        newTab("https://docs.google.com/spreadsheets/d/1c6SnHZg8ktjyMPjrnHjzCZZei5BPEdhX/")
        newTab("https://docs.google.com/spreadsheets/d/1keibC4lEYBMKx9SRfvhUoJYiHSiOrVwh/")
        newTab("https://docs.google.com/spreadsheets/d/1fRee5jd6rbO4JQd-OTMOGsUu1AxzDw2G/")
    if checkBool(name, ["Watch", "movies", "netflix"]):
        openGoogle()
        newTab(lofi)
        newTab("https://netflix.com")
        newTab("https://disneyplus.com")
        newTab("https://translate.google.com")
        
    if checkBool(name, ["english", "learn english"]):
        openGoogle()
        newTab(lofi)
        newTab("https://netflix.com")
        newTab("https://disneyplus.com")
        newTab("file:///C:/Users/Alexandre/Downloads/Campaigner%20profile.PDF")
        newTab("https://translate.google.com")
    if checkBool(name, ["unity", "make games"]):
        openGoogle()
        newTab(adventure_music)
        newTab(lofi)
        newTab("https://github.com/Ale10xp")
        newTab("https://keep.google.com")
        newTab("https://www.udemy.com/course/the-ultimate-guide-to-making-a-2d-strategy-game-in-unity/learn/lecture/16984222")
        newTab("https://youtu.be/9tePzyL6dgc")
        openProgram("Unity")
        openProgram("Visual Studio")
    if name == "now":
        print("\n Time now: " + str(dt.now()))
        print("\n \n Time Remining to Work: " + str(time_remaining))
        time.sleep(7)

    if checkBool(name, ["just music", "music"]):
        openGoogle()
        newTab(adventure_music)
        newTab(eletronic_music)

    if checkBool(name, ["blender", "blender"]):
        openProgram("Blender")
        setup("music")

def DataVisualizationTools(data):
    @interact_manual 
    def viz(funct = ["Distribuition Plot", "Bar Plot", "Scatter Plot"]):
        do(funct, data)

def do(functi, data):
    if functi == "Distribuition Plot":
        @interact_manual 
        def viz(x=list(data.select_dtypes('object').columns[1:])):
            #plt.rcParams['figure.figsize']=(25,20)
            sns.distplot( x= data[x])
            #plt.show()
    elif functi == "Bar Plot":
        #Categorical vs Continuous
        @interact_manual 
        def viz(x=list(data.select_dtypes('object').columns[1:]),
       y=list(data.select_dtypes('number').columns[1:])):
            #plt.rcParams['figure.figsize']=(25,20)
            sns.barplot( x= data[x], y= data[y])
            #plt.show()
    elif functi == "Scatter Plot":
        #Continuous vs Continuous
        @interact_manual 
        def viz(x=list(data.select_dtypes('number').columns[1:]),
            y=list(data.select_dtypes('number').columns[1:]), 
            color=list(data.select_dtypes('number').columns[1:])):
                sns.scatterplot( x= data[x], y= data[y], c= data[color])
                
