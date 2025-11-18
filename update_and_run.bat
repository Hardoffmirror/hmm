@echo off
echo ========================================
echo Update and Run
echo ========================================
echo.

REM Check if we're in the right directory
if not exist ".git" (
    echo [ERROR] Not in git repository!
    echo Please run this from the project root folder 'hmm'
    echo.
    pause
    exit /b 1
)

echo Updating from Git...
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS

echo.
echo Updating dependencies...
pip install -r requirements.txt --upgrade

echo.
echo Starting analyzer...
echo.
python tarot_analyzer.py

echo.
pause
