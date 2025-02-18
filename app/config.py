import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_default_key")

config = Config()
