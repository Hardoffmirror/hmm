@echo off
echo ========================================
echo Updating Project
echo ========================================
echo.

REM Check if we're in the right directory by checking key files
if not exist "web_app.py" (
    echo [ERROR] web_app.py not found!
    echo.
    echo Please run this script from the project root folder 'hmm'
    echo Current directory: %CD%
    echo.
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
    echo Current directory: %CD%
    echo.
    pause
    exit /b 1
)

echo Current directory: %CD%
echo.
echo Updating from Git...
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to update from Git
    echo.
    echo Possible reasons:
    echo - Not a git repository (did you download as ZIP?)
    echo - No internet connection
    echo - Git not installed
    echo.
    echo If you downloaded as ZIP, use 'git clone' instead
    echo Or manually download the latest version
    echo.
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
