@echo off
REM Build Call_Button_App into a Windows executable using PyInstaller

REM Step 1: Clean previous builds
echo Cleaning old build artifacts...
rmdir /s /q build
rmdir /s /q dist
del /q app.spec

REM Step 2: Activate virtual environment (optional)
REM call venv\Scripts\activate

REM Step 3: Install dependencies
echo Installing requirements...
pip install -r requirements.txt

REM Step 4: Build executable
echo Building executable with PyInstaller...
pyinstaller --noconfirm --windowed ^
  --add-data "sounds;sounds" ^
  --add-data "templates;templates" ^
  --add-data "static;static" ^
  --add-data "mpg123.exe;." ^
  app.py

REM Step 5: Notify user
echo Build complete. Executable is in the dist\ folder.
pause
