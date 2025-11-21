"""
Quick demo runner for hackathon presentation
"""

import subprocess
import sys
import os
from pathlib import Path

def check_requirements():
    """Check if required packages are installed"""
    try:
        import streamlit
        import google.generativeai
        print("✅ Required packages found")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Run: pip install -r requirements.txt")
        return False

def check_api_key():
    """Check if Google API key is set"""
    if os.getenv("GOOGLE_API_KEY") or "AIzaSyA58E56kqLge13tcJy1yoRpOXRKZ20duxc":
        print("✅ Google API key configured")
        return True
    else:
        print("❌ Google API key not found")
        print("Set environment variable: GOOGLE_API_KEY=your_key_here")
        return False

def create_demo_files():
    """Create demo files if they don't exist"""
    if not Path("demo_files").exists():
        print("📁 Creating demo files...")
        exec(open("demo_setup.py").read())
    else:
        print("✅ Demo files already exist")

def main():
    print("🚀 AI Business Automation Agent - Demo Launcher")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        return
    
    # Check API key
    if not check_api_key():
        print("\n💡 For demo purposes, you can:")
        print("1. Get a free Google AI API key at: https://aistudio.google.com/app/apikey")
        print("2. Set it as environment variable: GOOGLE_API_KEY=your_key_here")
        print("3. Or the app will use the configured key")
        return
    
    # Create demo files
    create_demo_files()
    
    print("\n🎯 Demo Instructions:")
    print("1. Upload one of the demo files from 'demo_files' folder")
    print("2. Click 'Analyze Document' to see AI in action")
    print("3. View results in the 'Results' tab")
    print("4. Download generated reports and emails")
    
    print("\n🌟 Key Demo Points to Highlight:")
    print("- Multi-format document processing (PDF, Word, images)")
    print("- AI-powered summarization and insights")
    print("- Automated email generation")
    print("- Task creation and workflow automation")
    print("- Professional business analysis")
    
    print("\n🚀 Starting Streamlit app...")
    print("Press Ctrl+C to stop the demo")
    
    # Launch Streamlit
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Demo stopped. Great job!")

if __name__ == "__main__":
    main()