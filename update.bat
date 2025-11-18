@echo off
echo ========================================
echo Updating Project
echo ========================================
echo.

echo Updating from Git...
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to update from Git
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
