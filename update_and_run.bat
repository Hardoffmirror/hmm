@echo off
echo ========================================
echo Update and Run Web Interface
echo ========================================
echo.

REM Check if we're in the right directory
if not exist "web_app.py" (
    echo [ERROR] web_app.py not found!
    echo Please run this from the project root folder 'hmm'
    echo Current directory: %CD%
    echo.
    pause
    exit /b 1
)

echo Current directory: %CD%
echo.
echo Updating from Git...
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS

echo.
echo Updating dependencies...
pip install -r requirements.txt --upgrade

echo.
echo Starting web interface...
echo Browser will open automatically
echo.
echo Press Ctrl+C to stop the server
echo.
python web_app.py

echo.
pause
