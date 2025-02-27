import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # API Key from .env
