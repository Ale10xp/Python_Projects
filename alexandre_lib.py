import time
import pyautogui as pg

from random import randint as rd
import random
import os 
import pyttsx3
import re

def say(text):
    engine = pyttsx3.init()
    text = [text]
    for i in text:
        engine.say(i)
        engine.runAndWait()

def randomList(itens):
    if itens:
        return random.choice(itens)

lofis = ["https://youtu.be/jhvUqV3qeC0", 
         "https://youtu.be/wtg7AetxuWo",
         "https://youtu.be/uUR4020kmrs", 
         "https://youtu.be/jrTMMG0zJyI",
         "https://youtu.be/6me17gGZYRg"]


adventure_musics = ["https://youtu.be/B7xai5u_tnk",
                    "https://youtu.be/cMg8KaMdDYo",
                    "https://youtu.be/j-2DGYNXRx0",
                    "https://youtu.be/wKRL7vkWMoc",
                    "https://youtu.be/p7ZsBPK656s",
                    "https://youtu.be/yJg-Y5byMMw",
                    "https://youtu.be/fiore9Z5iUg",
                    "https://youtu.be/qW33N_i7p3Y",
                    "https://youtu.be/qW33N_i7p3Y?t=550",
                    "https://youtu.be/qW33N_i7p3Y?t=349"]


adventure_music = randomList(adventure_musics)

lofi = randomList(lofis)



eletronic_musics =["https://youtu.be/vPUp5pzh8Mc", "https://youtu.be/fiore9Z5iUg"]
eletronic_music = randomList(eletronic_musics)

relaxing_musics = ["https://youtu.be/FaX64o71vGQ", "https://open.spotify.com"]
relaxing_music = randomList(relaxing_musics)


##IMPROVED BY OPEN AI 21/01/2023

def checkBool(check_item, list_of_items):
    return check_item.lower() in (item.lower() for item in list_of_items)

def newTab(url, _interval = 0.075):
    pg.hotkey("ctrlleft","t")
    time.sleep(1)
    pg.typewrite(url, interval = _interval)
    pg.press("enter")

def openGoogle(times = 5):
    #google
    winR("chrome")
    #pg.press("winleft")
    #pg.typewrite("Google", interval = 0.25)
    #pg.press("enter")
    time.sleep(times)
    pg.click(750, 550,duration =1)
    time.sleep(1)


def winR (text):
    pg.hotkey("winleft","r")
    if text is not None:
        pg.typewrite(text)
        pg.press("enter")


def openProgram(name):
    pg.press("winleft")
    pg.typewrite(name, interval = 0.25)
    pg.press("enter")
    time.sleep(1)
    #winR(name)

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


def shutdown_computer(time):
    os.system("shutdown /s /t {}".format(time))

                ####IMPROVED BY OPEN AI 21/01/2023

def setup(name, times = 45): 
    options = {
        "cursos": ["https://www.udemy.com/", "https://humanosforadacurva.com/courses", "https://membros.nucleoexpert.com/", "https://youtu.be/vPUp5pzh8Mc"],
        "games": ["https://www.metasrc.com/5v5/champion/swain/support", "https://web.whatsapp.com/", eletronic_music],
        "lofi": ["https://keep.google.com/", "https://calendar.google.com/", "https://open.spotify.com/"],
        "chat": ["https://instagram.com", "https://web.whatsapp.com", "https://facebook.com/", "https://web.telegram.org/k/", "https://photos.google.com"],
        "draw": ["https://pinterest.com", "https://youtube.com", adventure_music],
        "py": ["https://www.udemy.com/course/machine-learning-data-science-python/learn/lecture/26035392", adventure_music],
        "strategy": ["https://keep.google.com/", "https://calendar.google.com/", "https://docs.google.com/spreadsheets/d/1c6SnHZg8ktjyMPjrnHjzCZZei5BPEdhX/", "https://docs.google.com/spreadsheets/d/1keibC4lEYBMKx9SRfvhUoJYiHSiOrVwh/", "https://docs.google.com/spreadsheets/d/1fRee5jd6rbO4JQd-OTMOGsUu1AxzDw2G/"],
        "watch": ["https://netflix.com", "https://disneyplus.com", "https://translate.google.com"],
        "english": ["https://netflix.com", "https://disneyplus.com", "file:///C:/Users/Alexandre/Downloads/Campaigner%20profile%20-%20Alexandre%20-%20English%20Central.html"]
    }

    if name in options:
        openGoogle()
        for tab in options[name]:
            newTab(tab)
        if name == "lofi":
            Flux(20)
        elif name == "py":
            os.system("start jupyter notebook")
        elif name == "chat":
            say("Oh Right! I'm opening the chats for you. Whatsapp. Instagram an so on. Take a breath. enjoy.")
            openProgram("f.lux")            
        if "shutdown" in options.keys():
            time = input("How many minutes before shutting down? ")
            confirm = input("Are you sure you want to shut down the computer in {} minutes (y/n)? ".format(time))
            if confirm == 'y':
                shutdown_computer(time)
            else:
                print("Shutdown cancelled.")
                
