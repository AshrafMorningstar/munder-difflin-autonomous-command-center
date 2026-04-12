@echo off
title Munder Difflin Auto Installer
echo ======================================================================
echo   MUNDER DIFFLIN COMMAND CENTER - 1-CLICK AUTOMATED INSTALLER
echo ======================================================================

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python 3.10+ from https://python.org and check "Add to PATH".
    pause
    exit /b 1
)

echo [*] Launching automated Python setup script...
python "%~dp0install.py"

echo.
echo Setup finished. Press any key to start the Interactive Command Center...
pause >nul
python "%~dp0munder_command_center.py"
