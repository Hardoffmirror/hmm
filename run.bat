@echo off

REM Check if we're in the right directory
if not exist "tarot_analyzer.py" (
    echo [ERROR] tarot_analyzer.py not found!
    echo Please run this from the project root folder 'hmm'
    echo.
    pause
    exit /b 1
)

REM Quick run analyzer
python tarot_analyzer.py %*
pause
