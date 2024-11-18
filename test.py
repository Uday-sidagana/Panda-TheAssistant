import google.generativeai as genai
import os
from dotenv import load_dotenv
import time
load_dotenv()

my_api_key = os.getenv("GEMINI_API")


genai.configure(api_key=my_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text) 