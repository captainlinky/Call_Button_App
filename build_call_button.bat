@echo off
REM Build Call_Button_App into a single Windows executable using PyInstaller

REM Step 1: Clean previous builds
echo Cleaning old build artifacts...
rmdir /s /q build
rmdir /s /q dist
del /q app.spec

REM Step 2: Install dependencies
echo Installing Python packages from requirements.txt...
pip install -r requirements.txt

REM Step 3: Build single-file executable
echo Building single-file executable with PyInstaller...
pyinstaller --noconfirm --onefile --windowed ^
  --add-data "sounds\\alert.mp3;sounds" ^
  --add-data "templates\\;templates" ^
  --add-data "static\\;static" ^
  --add-data "mpg123.exe;." ^
  app.py

REM Step 4: Notify user
echo Build complete. Single executable is in the dist\ folder.
pause
