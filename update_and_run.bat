@echo off
echo ========================================
echo Update and Run
echo ========================================
echo.

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
