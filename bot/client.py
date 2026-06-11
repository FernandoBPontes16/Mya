from google import genai
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
#gemini = genai.Client(api_key=os.getenv("API_KEY"))
groq = Groq(api_key=os.getenv("API_KEY"))        