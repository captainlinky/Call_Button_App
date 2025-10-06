from flask import Flask, render_template, redirect, url_for
from datetime import datetime
import subprocess
import csv
import os
import pandas as pd

app = Flask(__name__)

LOG_FILE = 'event_log.csv'
ALERT_SOUND = 'alert.mp3'

def log_event(event_type):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_exists = os.path.exists(LOG_FILE)
    write_header = not file_exists or os.path.getsize(LOG_FILE) == 0

    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['timestamp', 'event_type'])
        writer.writerow([timestamp, event_type])

    print(f"[LOGGED] {event_type} at {timestamp}")

def play_sound():
    sound_path = os.path.join('sounds', ALERT_SOUND)
    try:
        subprocess.run(['mpg123', sound_path], check=True)
    except Exception as e:
        print(f"[ERROR] Sound playback failed: {e}")

@app.route('/trend')
def trend():
    try:
        import matplotlib
        matplotlib.use('Agg')  # Safe for headless environments
        import matplotlib.pyplot as plt
        from io import BytesIO
        import base64

        if not os.path.exists(LOG_FILE):
            raise FileNotFoundError(f"{LOG_FILE} not found")

        df = pd.read_csv(LOG_FILE)
        required_columns = {'timestamp', 'event_type'}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"CSV must contain columns: {required_columns}")

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')

        grouped = df.groupby(['date', 'event_type']).size().unstack(fill_value=0)
        grouped = grouped.reset_index()
    totals = df['event_type'].value_counts().to_dict()
    return render_template('trend.html', graph=img_base64, totals=totals)


        fig, ax = plt.subplots(figsize=(10, 6))
        for event_type in grouped.columns[1:]:
            ax.plot(grouped['date'], grouped[event_type], label=event_type, marker='o')

        ax.set_title('Event Frequency by Type')
        ax.set_xlabel('Date')
        ax.set_ylabel('Count')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        buf = BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)

        return render_template('trend.html', graph=img_base64)

    except Exception as e:
        return f"<h1>Error in /trend route:</h1><pre>{e}</pre>", 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_event/<event_type>')
def log_and_notify(event_type):
    log_event(event_type)
    play_sound()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

