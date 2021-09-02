import webbrowser
import datetime
import speech_recognition as sr
import time
from selenium import webdriver
import pyttsx3
import wikipedia
import os
import urllib.request
import urllib.parse
import re


def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    time.sleep(1)
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            time.sleep(1)
            print("Recognizing")
            query = r.recognize_google(audio, language = 'en-in')
            query = query.lower()
            print(f"user said: {query}")
    except:
        print("Please say that again")
        takeCommand()
        time.sleep(1)
    return query


r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

print("Initializing Friday")
speak("Initializing Friday ")
chrome_path = 'Enter your path to chrome here' # Here goes your path to chrome.

while True:
    query = takeCommand()

    if 'goodbye friday' in query:
        break


    if 'wikipedia' in query:
        speak('Searching wikipidea')
        query = query.replace("wikipidea","")
        results = wikipedia.summary(query,sentences = 2)
        print(results)
        speak(results)

    elif 'open google' in query:
        url = 'google.com'
        webbrowser.get(chrome_path).open(url)

    elif 'youtube' in query:
        query = query.replace("youtube","")
        query = query.replace(" ","+")
        
        html_content = urllib.request.urlopen('http://www.youtube.com/results?q=%s'%query)
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        
        webbrowser.get(chrome_path).open('https://www.youtube.com/watch?v=%s'%search_results[0])

    elif 'google map' in query:
        query = query.replace("google map","")
        webbrowser.get(chrome_path).open('google.com/maps/place/?q=%s'%query)

    elif 'play music' in query:
        songs = os.listdir("E:\\Music")
        
        speak("What do you want to listen?")
        name = takeCommand()
        for i in songs:
            if name in i.lower():
                os.startfile(os.path.join("Path to folder",i)) # Enter the path to the folder in which songs are kept.

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(strTime)

    elif 'google search' in query:
        try: 
            from googlesearch import search 
        except ImportError:  
            print("No module named 'google' found") 
        
        # to search 
        query = query.replace("google search","")
        
        for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
            webbrowser.get(chrome_path).open("https://google.com/search?q=%s"%query) 
            
    elif 'spotify' in query:
        
        speak("What do you want to listen?")
        name = takeCommand()
        browser = webdriver.Chrome(executable_path=r'C:\Users\Dell\Downloads\chromedriver_win32\chromedriver.exe')
        browser.get('https://accounts.spotify.com/en/login')

        username = browser.find_element_by_id("login-username")
        password = browser.find_element_by_id("login-password")
        username.send_keys('Enter your spotify username here') #spotify credentials
        password.send_keys('Enter your spotify password') #spotify credentials
        submit = browser.find_element_by_id("login-button")
        submit.click()
        time.sleep(2)
        browser.get('https://open.spotify.com/search/%s'%name)
        time.sleep(2)
        play = browser.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/img')
        play.click()
        continue
    
    else :
        speak("Didn't get you, can you please say that again?")
