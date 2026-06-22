@echo off
title Munder Difflin Auto Command Center
echo ========================================================
echo   MUNDER DIFFLIN - FULLY AUTOMATED ZERO-CLICK COMMAND CENTER
echo ========================================================

:: 1. Global AI Gateway Endpoints & Defaults
if "%OPENAI_API_BASE%"=="" set OPENAI_API_BASE=http://localhost:20128/v1
if "%OPENAI_BASE_URL%"=="" set OPENAI_BASE_URL=http://localhost:20128/v1
if "%FREELLMAPI_URL%"=="" set FREELLMAPI_URL=http://127.0.0.1:31415
if "%ANTHROPIC_BASE_URL%"=="" set ANTHROPIC_BASE_URL=http://127.0.0.1:31415

:: Load local keys from API_KEYS.txt if present
if exist "%~dp0API_KEYS.txt" (
    for /f "tokens=1,* delims==" %%a in ('type "%~dp0API_KEYS.txt" ^| findstr /r "^[A-Z]"') do (
        set "%%a=%%b"
    )
)

:: 2. Launch FreeLLMAPI Gateway if not running
tasklist /FI "IMAGENAME eq FreeLLMAPI.exe" 2>NUL | find /I /N "FreeLLMAPI.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [*] FreeLLMAPI Gateway is already running.
) else (
    echo [*] Launching FreeLLMAPI Gateway...
    if exist "C:\Users\Admin\AppData\Local\Programs\freellmapi-desktop\FreeLLMAPI.exe" (
        start "" "C:\Users\Admin\AppData\Local\Programs\freellmapi-desktop\FreeLLMAPI.exe"
    )
)

:: 3. Launch OmniRoute AI Gateway if not running
tasklist /FI "IMAGENAME eq OmniRoute.exe" 2>NUL | find /I /N "OmniRoute.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [*] OmniRoute Gateway is already running.
) else (
    echo [*] Launching OmniRoute Gateway...
    if exist "C:\Program Files\OmniRoute\OmniRoute.exe" (
        start "" "C:\Program Files\OmniRoute\OmniRoute.exe"
    )
)

:: 4. Launch Munder Difflin Desktop Application if not running
tasklist /FI "IMAGENAME eq Munder Difflin.exe" 2>NUL | find /I /N "Munder Difflin.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [*] Munder Difflin Desktop is already running.
) else (
    echo [*] Starting Munder Difflin Desktop Application...
    if exist "C:\Program Files\Munder Difflin\Munder Difflin.exe" (
        start "" "C:\Program Files\Munder Difflin\Munder Difflin.exe"
    )
)

:: 5. Launch Autonomous Office Floor Daemon
echo [*] Starting Munder Difflin Autonomous Multi-Agent Daemon...
start "Munder Difflin Floor Daemon" /min python "%~dp0munder_autonomous_daemon.py"

echo ========================================================
echo   [SUCCESS] COMMAND CENTER ACTIVE:
echo   - OmniRoute Gateway:   %OPENAI_API_BASE%
echo   - FreeLLMAPI Gateway:  %FREELLMAPI_URL%
echo   - Multi-Agent Daemon:  Running in background
echo ========================================================
