@echo off
chcp 65001 >nul
REM Быстрый запуск анализатора / Quick run analyzer
python tarot_analyzer.py %*
pause
