@echo off
echo ========================================
echo League Detection Test
echo ========================================
echo.

REM Check if we're in the right directory
if not exist "test_leagues.py" (
    echo [ERROR] test_leagues.py not found!
    echo Please run this from the project root folder 'hmm'
    echo.
    pause
    exit /b 1
)

echo Testing which league names work on poe.ninja...
echo This will take about 30 seconds.
echo.

python test_leagues.py

echo.
pause
