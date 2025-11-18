@echo off
echo ========================================
echo Updating Project
echo ========================================
echo.

REM Check if we're in the right directory
if not exist ".git" (
    echo [ERROR] Not in git repository!
    echo.
    echo Please run this script from the project root folder 'hmm'
    echo Example: cd C:\path\to\hmm
    echo          update.bat
    echo.
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo [ERROR] requirements.txt not found!
    echo.
    echo Please run this script from the project root folder 'hmm'
    echo.
    pause
    exit /b 1
)

echo Updating from Git...
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to update from Git
    echo Check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo Updating dependencies...
pip install -r requirements.txt --upgrade
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to update dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Update complete!
echo ========================================
echo.
pause
