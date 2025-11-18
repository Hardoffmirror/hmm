@echo off
chcp 65001 >nul
echo ========================================
echo PoE Divination Card Analyzer
echo Установка и запуск / Install and Run
echo ========================================
echo.

REM Проверка Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ОШИБКА] Python не найден!
    echo [ERROR] Python not found!
    echo.
    echo Установите Python с https://www.python.org/downloads/
    echo При установке отметьте "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo [OK] Python найден / Python found
python --version
echo.

REM Установка зависимостей
echo Установка зависимостей / Installing dependencies...
echo.
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo [ОШИБКА] Не удалось установить зависимости
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Установка завершена! / Installation complete!
echo ========================================
echo.
echo Запуск анализатора... / Running analyzer...
echo.

REM Запуск программы
python tarot_analyzer.py

echo.
echo ========================================
echo Готово! / Done!
echo ========================================
pause
