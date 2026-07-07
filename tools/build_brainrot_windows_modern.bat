@echo off
setlocal

cd /d "%~dp0\.."

where python >nul 2>nul
if errorlevel 1 goto no_python

where make >nul 2>nul
if errorlevel 1 goto no_make

rem Try common devkitPro paths first.
if exist "C:\devkitPro\devkitARM\bin\arm-none-eabi-gcc.exe" (
    set "DEVKITPRO=C:\devkitPro"
    set "DEVKITARM=C:\devkitPro\devkitARM"
    set "PATH=C:\devkitPro\devkitARM\bin;%PATH%"
)

if exist "C:\devkitPro\msys2\opt\devkitpro\devkitARM\bin\arm-none-eabi-gcc.exe" (
    set "DEVKITPRO=C:\devkitPro\msys2\opt\devkitpro"
    set "DEVKITARM=C:\devkitPro\msys2\opt\devkitpro\devkitARM"
    set "PATH=C:\devkitPro\msys2\opt\devkitpro\devkitARM\bin;%PATH%"
)

if exist "C:\msys64\opt\devkitpro\devkitARM\bin\arm-none-eabi-gcc.exe" (
    set "DEVKITPRO=C:\msys64\opt\devkitpro"
    set "DEVKITARM=C:\msys64\opt\devkitpro\devkitARM"
    set "PATH=C:\msys64\opt\devkitpro\devkitARM\bin;%PATH%"
)

rem If PowerShell/devkitPro added pacman but not compiler PATH, search a little deeper.
where arm-none-eabi-gcc >nul 2>nul
if errorlevel 1 (
    for /f "delims=" %%G in ('dir /b /s "C:\arm-none-eabi-gcc.exe" "C:\devkitPro\arm-none-eabi-gcc.exe" "C:\msys64\arm-none-eabi-gcc.exe" 2^>nul') do (
        set "GCC_PATH=%%G"
        goto found_gcc
    )
    goto no_arm
)
goto have_gcc

:found_gcc
for %%D in ("%GCC_PATH%") do set "GCC_BIN=%%~dpD"
set "PATH=%GCC_BIN%;%PATH%"

:have_gcc
arm-none-eabi-gcc --version
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
echo arm-none-eabi-gcc was not found in PATH or common devkitPro folders.
echo Try this in PowerShell:
echo Get-ChildItem C:\ -Filter arm-none-eabi-gcc.exe -Recurse -ErrorAction SilentlyContinue ^| Select-Object -First 5 FullName
pause
goto end

:error
echo.
echo Build failed. Copy the first error above and send it to ChatGPT.
pause

:end
endlocal
