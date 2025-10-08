@echo off
SETLOCAL

:: 🧪 Check for Python
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org and try again.
    EXIT /B 1
)

:: 📦 Check for pip
pip --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ pip is not installed or not in PATH.
    echo Please reinstall Python and ensure pip is included.
    EXIT /B 1
)

:: 🔍 Check for PyInstaller
pip show pyinstaller >nul 2>&1
IF ERRORLEVEL 1 (
    echo 📦 Installing PyInstaller...
    pip install pyinstaller
)

:: 🧹 Clean previous builds
echo 🧹 Cleaning old build artifacts...
rmdir /s /q dist
rmdir /s /q build
del App.spec >nul 2>&1

:: 🚧 Build the EXE
echo 🚧 Building Call_Button_App executable...
pyinstaller --onefile --windowed App.py ^
  --add-data "templates;templates" ^
  --add-data "static;static" ^
  --add-data "sounds;sounds" ^
  --collect-all flask

:: ✅ Completion message
echo ✅ Build complete. Check the dist\ folder for Call_Button_App.exe

ENDLOCAL
pause
