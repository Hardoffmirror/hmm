@echo off
echo ========================================
echo PoE Divination Card Analyzer
echo Web Interface
echo ========================================
echo.

REM Check if we're in the right directory
if not exist "web_app.py" (
    echo [ERROR] web_app.py not found!
    echo Please run this from the project root folder 'hmm'
    echo Current directory: %CD%
    echo.
    echo Try: cd C:\path\to\hmm
    echo      run_web.bat
    echo.
    pause
    exit /b 1
)

echo Current directory: %CD%
echo.
echo Starting web server...
echo Browser will open automatically
echo.
echo Press Ctrl+C to stop the server
echo.
python web_app.py
pause
