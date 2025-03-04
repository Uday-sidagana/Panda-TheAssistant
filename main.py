import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from bs4 import BeautifulSoup
#------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#------
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

my_api_key = os.getenv("GEMINI_API")




def call_gemini_api(prompt):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={my_api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        try:
            return result['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError):
            return "Error: Unable to extract AI response."
    else:
        return f"Error: {response.status_code}, {response.text}"


def audio_recognize_in_func():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    audio_search = r.recognize_google(audio)
    return audio_search


def functionalities(command):
    if "instagram" in command.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "github" in command.lower():
        webbrowser.open("https://www.github.com/")
    elif "amazon" in command.lower():
        webbrowser.open("https://www.amazon.in/")

    elif "wikipedia" in command.lower():
        wiki_search= audio_recognize_in_func()
        webbrowser.open(f"https://en.wikipedia.org/wiki/{wiki_search}")
    
    elif "youtube" in command.lower():
        youtube_search= audio_recognize_in_func()
        webbrowser.open(f"https://www.youtube.com/results?search_query={youtube_search}")

    elif "google" in command.lower():

        driver = webdriver.Chrome()  
        driver.get("https://www.google.com/")  
        search_box = driver.find_element(By.CLASS_NAME, "gLFyf") #This is the Class name of Google Search-Box

        google_search= audio_recognize_in_func()
        search_box.send_keys(google_search)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.quit()

    elif "dictionary" in command.lower():
        dict_word = audio_recognize_in_func()
        print(dict_word)
        url= f"https://www.dictionary.com/browse/{dict_word}"

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        first_div = soup.find('div', class_="NZKOFkdkcvYgD3lqOIJw")
        assistant_text = first_div.get_text()
        print(assistant_text)

        engine = pyttsx3.init(driverName='nsss')
        volume = engine.getProperty('volume')   
        engine.setProperty('volume',1.0)
        engine.setProperty('rate', 200)
        print("Speaking now")
        engine.say(assistant_text)
        engine.runAndWait()

    else:
        while True:
            print("Generating...")

            response = call_gemini_api(command)
            print(response.text)

            # time.sleep(10)

            command = audio_recognize_in_func()
            print(command)

            if "stop" in command.lower() or "exit" in command.lower():
                print("Your AI Agent stopped...")
                break

    

assistant_audio= audio_recognize_in_func()
print(assistant_audio)


if "panda" in assistant_audio.lower():
    # engine = pyttsx3.init(driverName='nsss')
    # volume = engine.getProperty('volume')   
    
    # engine.setProperty('volume',1.0)
    # engine.setProperty('rate', 150)
    # print("Speaking now")
    # engine.say("Hey Uday!")
    # engine.runAndWait()
    while True:
        print("Can i help you with anything? Say Stop or Exit to close the chat")

        command = audio_recognize_in_func()
        if "stop" in command or "exit" in command:
            print("Bye Bye Uday... Hehe...")
            break
        
        functionalities(command)

        

       


