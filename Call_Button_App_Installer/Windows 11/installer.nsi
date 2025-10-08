; NSIS Installer Script for Caregiver Alert Panel

Name "Caregiver Alert Panel"
OutFile "CaregiverInstaller.exe"
InstallDir "$PROGRAMFILES\CaregiverAlertPanel"
Icon "Call_Button.ico"
ShowInstDetails show

Section "Install"
  SetOutPath "$INSTDIR"
  File "Call_Button.exe"
  File /r "static\*"
  File /r "templates\*"
  File /r "sounds\*"


  CreateShortCut "$DESKTOP\Caregiver Alert Panel.lnk" "$INSTDIR\Call_Button.exe" "" "$INSTDIR\caregiver_icon.ico"
SectionEnd

Function .onInstSuccess
  MessageBox MB_OK|MB_ICONINFORMATION "✅ Installation complete!\n\nThe Caregiver Alert Panel is now listening.\nOpen your browser and go to:\n\nhttp://127.0.0.1:5000"
FunctionEnd


