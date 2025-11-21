@echo off
echo ========================================
echo   AI Business Automation Agent
echo   Starting Streamlit Application...
echo ========================================
echo.

REM Check if dependencies are installed
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo Starting the app...
echo Press Ctrl+C to stop
echo.

streamlit run app.py
