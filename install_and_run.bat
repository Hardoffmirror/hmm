@echo off
echo ========================================
echo PoE Divination Card Analyzer
echo Install and Run
echo ========================================
echo.

REM Check if we're in the right directory
if not exist "requirements.txt" (
    echo [ERROR] requirements.txt not found!
    echo Please run this from the project root folder 'hmm'
    echo.
    pause
    exit /b 1
)

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo.
    echo Install Python from https://www.python.org/downloads/
    echo Check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Install dependencies
echo Installing dependencies...
echo.
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo Running analyzer...
echo.

REM Run program
python tarot_analyzer.py

echo.
echo ========================================
echo Done!
echo ========================================
pause
