import os
from dotenv import load_dotenv

load_dotenv() # loads all env variables 

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")
