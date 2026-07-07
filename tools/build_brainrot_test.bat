@echo off
setlocal

cd /d "%~dp0\.."

python tools\apply_brainrot_test_build.py
if errorlevel 1 goto error

make
if errorlevel 1 goto error

echo.
echo Done. Open pokefirered.gba in mGBA.
goto end

:error
echo.
echo Build failed. Copy the error above and send it to ChatGPT.
pause

:end
endlocal
