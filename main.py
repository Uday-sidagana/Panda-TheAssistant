import speech_recognition as sr
import pyttsx3
import webbrowser
#------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

assistant_call = r.recognize_google(audio)
print(assistant_call)

if "panda" in assistant_call.lower():
    # engine = pyttsx3.init(driverName='nsss')
    # volume = engine.getProperty('volume')   
    
    # engine.setProperty('volume',1.0)
    # engine.setProperty('rate', 150)
    # print("Speaking now")
    # engine.say("Hey Uday!")
    # engine.runAndWait()
    print("Hey UDAY!!")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    command = r.recognize_google(audio)
    
    functionalities(command)


    
