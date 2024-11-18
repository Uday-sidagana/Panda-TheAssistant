import google.generativeai as genai
import os
from dotenv import load_dotenv
import time
load_dotenv()

my_api_key = os.getenv("GEMINI_API")


genai.configure(api_key= my_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

ai_command = input("type...")




if "stop" not in ai_command.lower() and "exit" not in ai_command.lower():

            print("Generating...")

            response = model.generate_content(ai_command)
            print(response.text)

            time.sleep(5)



else:
    print("Your AI Agent stopped...")