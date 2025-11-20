import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # API Keys
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    
    # Database
    DATABASE_URL = "sqlite:///./auto_ceo.db"
    
    # File Upload Settings
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.png', '.jpg', '.jpeg'}
    
    # AI Settings
    DEFAULT_MODEL = "gpt-3.5-turbo"
    MAX_TOKENS = 1000
    TEMPERATURE = 0.7
    
    # App Settings
    APP_TITLE = "AI Business Automation Agent"
    APP_DESCRIPTION = "Your AI-powered business automation assistant"