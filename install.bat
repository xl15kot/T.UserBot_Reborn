@echo off
title T.UserBot Reborn v0.3 Beta - Installer
color 0A

echo ============================================================
echo   T.UserBot Reborn v0.3 Beta - Installer
echo ============================================================
echo.

echo Do you have Python installed?
echo.
set /p has_python="Do you have Python? (y/n): "

if /i "%has_python%"=="y" (
    echo.
    echo [OK] Installing libraries...
    pip install telethon
    pip install requests
    pip install Pillow
    pip install PyQt5
    goto :create_files
)

if /i "%has_python%"=="n" (
    echo.
    echo [INFO] Python not found. Starting Python installer...
    echo.
    
    if exist "%~dp0python_inst.exe" (
        echo Running python_inst.exe...
        start /wait "" "%~dp0python_inst.exe"
        
        echo.
        echo Python installation completed.
        echo.
        echo Now installing libraries...
        python -m pip install telethon
        python -m pip install requests
        python -m pip install Pillow
        python -m pip install PyQt5
    ) else (
        echo [ERROR] python_inst.exe not found!
        echo Please download Python from: https://www.python.org/downloads/
        echo and save python_inst.exe to this folder
        echo.
        pause
        exit /b 1
    )
) else (
    echo [ERROR] Invalid input! Please enter y or n
    pause
    exit /b 1
)

:create_files
echo.
echo Creating run.bat...
(
echo @echo off
echo cd /d "%%~dp0"
echo python main.py
echo pause
) > run.bat

echo.
echo Creating desktop shortcut...
set SCRIPT=%TEMP%\make_shortcut.vbs
(
echo Set oWS = WScript.CreateObject("WScript.Shell")
echo sLinkFile = oWS.ExpandEnvironmentStrings("%USERPROFILE%\Desktop\T.UserBot Reborn v0.3 Beta.lnk")
echo Set oLink = oWS.CreateShortcut(sLinkFile)
echo oLink.TargetPath = oWS.ExpandEnvironmentStrings("%CD%\run.bat")
echo oLink.WorkingDirectory = oWS.ExpandEnvironmentStrings("%CD%")
echo oLink.Save
) > %SCRIPT%
cscript //nologo %SCRIPT%
del %SCRIPT%

echo.
echo ============================================================
echo   Installation complete!
echo ============================================================
echo.
echo Run the bot: double-click run.bat or desktop shortcut
echo.
pause