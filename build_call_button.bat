@echo off
SETLOCAL

:: Check for Python
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org and try again.
    EXIT /B 1
)

:: Check for pip
pip --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ pip is not installed or not in PATH.
    echo Please reinstall Python and ensure pip is included.
    EXIT /B 1
)

:: Install PyInstaller if missing
pip show pyinstaller >nul 2>&1
IF ERRORLEVEL 1 (
    echo 📦 Installing PyInstaller...
    pip install pyinstaller
)

:: Build the EXE
echo 🚧 Building Call_Button_App executable...
pyinstaller --onefile --windowed Call_Button_App.py \
  --add-data "templates;templates" \
  --add-data "static;static" \
  --add-data "sounds;sounds"


echo ✅ Build complete. Check the dist\ folder for your .exe file.

ENDLOCAL
pause
