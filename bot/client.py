from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
gemini = genai.Client(api_key=os.getenv("API_KEY"))        