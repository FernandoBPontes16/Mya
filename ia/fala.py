from google import genai
from google.genai import types
import sounddevice as sd 
import numpy as np  
import os
from ia import client
from dotenv import load_dotenv

load_dotenv()
client = client.genai.Client(api_key=os.getenv("API_KEY"))