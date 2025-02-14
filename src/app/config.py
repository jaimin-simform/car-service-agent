import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration settings"""
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-default-api-key")
    SMTP_USERNAME = os.getenv("SMTP_USERNAME", "your-email@example.com")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "your-email-password")
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.example.com")
    SMTP_PORT = os.getenv("SMTP_PORT", 465)
    GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_FILE", "src/credentials.json")

# Create a config instance
config = Config()
