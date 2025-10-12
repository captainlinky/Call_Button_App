from flask import Flask, render_template, redirect, url_for, send_file, Response, request
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv
import subprocess
import platform
from plyer import notification

app = Flask(__name__)

# ✅ Safe file paths
BASE_DIR = os.path.join(os.environ['USERPROFILE'], 'Documents', 'Call_Button_App')
os.makedirs(BASE_DIR, exist_ok=True)

LOG_FILE = os.path.join(BASE_DIR, 'event_log.csv')
TREND_IMAGE = os.path.join(BASE_DIR, 'trend_graph.png')
ALERT_SOUND = os.path.join('sounds', 'alert.mp3')

# ✅ Popup notification
def show_popup(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Call Button App",
            timeout=5
        )
    except Exception as e:
        print(f"[ERROR] Notification failed: {e}")

# ✅ Sound playback
def play_sound():
    try:
        subprocess.run(['mpg123.exe', ALERT_SOUND], check=True)
    except Exception as e:
        print(f"[ERROR] Sound playback failed: {e}")

# ✅ Log event
def log_event(event_type):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_exists = os.path.exists(LOG_FILE)
    write_header = not file_exists or os.path.getsize(LOG_FILE) == 0

    try:
        with open(LOG_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(['timestamp', 'event_type'])
            writer.writerow([timestamp, event_type])
        print(f"[LOGGED] {event_type} at {timestamp}")
    except Exception as e:
        print(f"[ERROR] Failed to write to log file: {e}")

# ✅ Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_event/<event_type>')
def log_and_notify(event_type):
    log_event(event_type)
    play_sound()
    show_popup("Care Alert", f"Event triggered: {event_type}")
    return redirect(url_for('index'))

@app.route('/trend')
def show_trend():
    try:
        df = pd.read_csv(LOG_FILE)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')
        grouped = df.groupby(['date', 'event_type']).size().unstack(fill_value=0)

        plt.figure(figsize=(10, 6))
        grouped.plot(kind='bar', stacked=True)
        plt.title('Care Event Trends')
        plt.xlabel('Date')
        plt.ylabel('Event Count')
        plt.tight_layout()
        plt.savefig(TREND_IMAGE)

        return send_file(TREND_IMAGE, mimetype='image/png')
    except Exception as e:
        return f"<h3>Error generating trend graph: {e}</h3>"

@app.route('/export')
def export_trend():
    range_param = request.args.get('range', '7d')
    now = pd.Timestamp.now()

    if range_param == '24h':
        cutoff = now - pd.Timedelta(hours=24)
    elif range_param == '30d':
        cutoff = now - pd.Timedelta(days=30)
    else:
        cutoff = now - pd.Timedelta(days=7)

    try:
        df = pd.read_csv(LOG_FILE)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df[df['timestamp'] >= cutoff]
        df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')

        grouped = df.groupby(['date', 'event_type']).size().unstack(fill_value=0).reset_index()
        csv_data = grouped.to_csv(index=False)

        return Response(
            csv_data,
            mimetype='text/csv',
            headers={"Content-Disposition": f"attachment;filename=trend_{range_param}.csv"}
        )
    except Exception as e:
        return Response(f"Error exporting CSV: {e}", status=500)

if __name__ == '__main__':
    app.run(debug=True)
