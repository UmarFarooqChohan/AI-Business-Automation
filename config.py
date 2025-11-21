import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # API Keys - Try Streamlit secrets first, then environment variable
    @staticmethod
    def get_api_key():
        try:
            import streamlit as st
            if hasattr(st, 'secrets') and 'GOOGLE_API_KEY' in st.secrets:
                return st.secrets['GOOGLE_API_KEY']
        except:
            pass
        return os.getenv("GOOGLE_API_KEY")
    
    GOOGLE_API_KEY: Optional[str] = get_api_key.__func__()
    
    # Database
    DATABASE_URL = "sqlite:///./auto_ceo.db"
    
    # File Upload Settings
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.png', '.jpg', '.jpeg'}
    
    # AI Settings
    DEFAULT_MODEL = "gemini-2.5-flash"
    MAX_TOKENS = 1000
    TEMPERATURE = 0.7
    
    # App Settings
    APP_TITLE = "AI Business Automation Agent"
    APP_DESCRIPTION = "Your AI-powered business automation assistant"