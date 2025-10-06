import subprocess
import os

# Patch environment for desktop session
os.environ['DBUS_SESSION_BUS_ADDRESS'] = os.popen('echo $DBUS_SESSION_BUS_ADDRESS').read().strip()

# Sound path
sound_path = 'static/alert.mp3'  # Adjust if needed

# Play sound
try:
    subprocess.Popen(['paplay', sound_path], env=os.environ)
    print("Sound triggered.")
except Exception as e:
    print(f"Sound failed: {e}")

# Show notification
try:
    subprocess.Popen(['notify-send', 'Test Alert', 'This is a manual test'], env=os.environ)
    print("Notification triggered.")
except Exception as e:
    print(f"Notification failed: {e}")

