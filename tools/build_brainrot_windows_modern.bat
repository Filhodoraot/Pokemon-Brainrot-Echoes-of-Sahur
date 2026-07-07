@echo off
setlocal

cd /d "%~dp0\.."

where python >nul 2>nul
if errorlevel 1 goto no_python

where make >nul 2>nul
if errorlevel 1 goto no_make

where arm-none-eabi-gcc >nul 2>nul
if errorlevel 1 goto no_arm

python tools\apply_brainrot_test_build.py
if errorlevel 1 goto error

python tools\patch_brainrot_trainers.py
if errorlevel 1 goto error

make firered_modern
if errorlevel 1 goto error

echo.
echo Done. Open pokefirered_modern.gba in mGBA.
goto end

:no_python
echo Python was not found. Install Python 3 and mark "Add Python to PATH".
pause
goto end

:no_make
echo make was not found. Install devkitPro/devkitARM and open this from its MSYS2/devkitPro shell, or add make to PATH.
pause
goto end

:no_arm
echo arm-none-eabi-gcc was not found. Install devkitPro/devkitARM and open this from its MSYS2/devkitPro shell.
pause
goto end

:error
echo.
echo Build failed. Copy the first error above and send it to ChatGPT.
pause

:end
endlocal
