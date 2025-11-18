@echo off
chcp 65001 >nul
echo ========================================
echo Обновление проекта / Updating project
echo ========================================
echo.

echo Обновление из Git...
git pull origin claude/tarot-price-analyzer-014hS12tobbrAzrbfTky1CRS
if errorlevel 1 (
    echo.
    echo [ОШИБКА] Не удалось обновить из Git
    echo [ERROR] Failed to update from Git
    pause
    exit /b 1
)

echo.
echo Обновление зависимостей...
pip install -r requirements.txt --upgrade
if errorlevel 1 (
    echo.
    echo [ОШИБКА] Не удалось обновить зависимости
    echo [ERROR] Failed to update dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Обновление завершено! / Update complete!
echo ========================================
echo.
pause
