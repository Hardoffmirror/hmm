@echo off
chcp 65001 >nul
echo ========================================
echo Обновление и запуск / Update and run
echo ========================================
echo.

echo Обновление из Git...
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS

echo.
echo Обновление зависимостей...
pip install -r requirements.txt --upgrade

echo.
echo Запуск анализатора...
echo.
python tarot_analyzer.py

echo.
pause
