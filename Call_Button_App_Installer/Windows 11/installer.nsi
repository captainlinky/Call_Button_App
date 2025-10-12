; Call_Button_App Installer
; Requires NSIS (https://nsis.sourceforge.io)

Name "Call Button App"
OutFile "Call_Button_App_Installer.exe"
InstallDir "$PROGRAMFILES\Call_Button_App"
RequestExecutionLevel user
SetCompress auto
SetCompressor lzma

;--------------------------------
; Interface

Page directory
Page instfiles

;--------------------------------
; Installer Sections

Section "Install"

  ; Create installation directory
  SetOutPath "$INSTDIR"

  ; Copy files
  File "dist\app.exe"
  File /r "sounds\*.*"
  File /r "templates\*.*"
  File /r "static\*.*"
  File "mpg123.exe"

  ; Create shortcuts
  CreateDirectory "$SMPROGRAMS\Call_Button_App"
  CreateShortCut "$SMPROGRAMS\Call_Button_App\Call_Button_App.lnk" "$INSTDIR\app.exe"
  CreateShortCut "$DESKTOP\Call_Button_App.lnk" "$INSTDIR\app.exe"

  ; Auto-run on startup
  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Run" "Call_Button_App" "$INSTDIR\app.exe"

  ; Write uninstall info
  WriteUninstaller "$INSTDIR\Uninstall.exe"

SectionEnd

;--------------------------------
; Uninstaller Section

Section "Uninstall"

  Delete "$INSTDIR\app.exe"
  Delete "$INSTDIR\mpg123.exe"
  RMDir /r "$INSTDIR\sounds"
  RMDir /r "$INSTDIR\templates"
  RMDir /r "$INSTDIR\static"

  Delete "$SMPROGRAMS\Call_Button_App\Call_Button_App.lnk"
  Delete "$DESKTOP\Call_Button_App.lnk"
  Delete "$INSTDIR\Uninstall.exe"
  DeleteRegValue HKCU "Software\Microsoft\Windows\CurrentVersion\Run" "Call_Button_App"
  RMDir "$SMPROGRAMS\Call_Button_App"
  RMDir "$INSTDIR"

SectionEnd

;--------------------------------
; Post-Install Instructions

Function .onInstSuccess
  MessageBox MB_OK "✅ Installation complete!\n\nYou can launch Call Button App from your desktop or Start Menu.\n\nIt will auto-run on startup. If you don't hear sound or see popups, check your system volume and notification settings."
FunctionEnd

