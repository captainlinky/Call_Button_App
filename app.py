from flask import Flask, render_template, redirect, url_for
from datetime import datetime
import subprocess
import csv
import os
import pandas as pd

from plyer import notification
import platform

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

import platform
import subprocess
import os

def play_sound():
    sound_path = os.path.join('sounds', ALERT_SOUND)
    system = platform.system()

    if system == 'Windows':
        mpg123_path = os.path.join(os.getcwd(), 'mpg123.exe')
        creation_flags = subprocess.CREATE_NO_WINDOW
    else:
        mpg123_path = 'mpg123'
        creation_flags = 0  # No effect on Linux/macOS

    try:
        subprocess.run([mpg123_path, sound_path], check=True, creationflags=creation_flags)
    except Exception as e:
        print(f"[ERROR] Sound playback failed: {e}")



@app.route('/trend')
def trend():
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import numpy as np
        from io import BytesIO
        import base64
        from flask import request

        # Get time range from query string
        range_param = request.args.get('range', '7d')
        now = pd.Timestamp.now()

        if range_param == '24h':
            cutoff = now - pd.Timedelta(hours=24)
        elif range_param == '30d':
            cutoff = now - pd.Timedelta(days=30)
        else:  # default to 7d
            cutoff = now - pd.Timedelta(days=7)

        # Load and filter data
        if not os.path.exists(LOG_FILE):
            raise FileNotFoundError(f"{LOG_FILE} not found")

        df = pd.read_csv(LOG_FILE)
        required_columns = {'timestamp', 'event_type'}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"CSV must contain columns: {required_columns}")

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df[df['timestamp'] >= cutoff]
        df['date'] = df['timestamp'].dt.strftime('%Y-%m-%d')

        grouped = df.groupby(['date', 'event_type']).size().unstack(fill_value=0).reset_index()
        totals = df['event_type'].value_counts().to_dict()

        # Create grouped bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        x = np.arange(len(grouped['date']))
        bar_width = 0.15
        event_types = grouped.columns[1:]
        offsets = np.linspace(-bar_width * (len(event_types) - 1) / 2,
                              bar_width * (len(event_types) - 1) / 2,
                              len(event_types))

        for i, event_type in enumerate(event_types):
            ax.bar(x + offsets[i], grouped[event_type], width=bar_width, label=event_type)

        ax.set_xticks(x)
        ax.set_xticklabels(grouped['date'], rotation=45)
        ax.set_title('Event Frequency by Type')
        ax.set_xlabel('Date')
        ax.set_ylabel('Count')
        ax.legend()
        plt.tight_layout()

        # Encode graph
        buf = BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)

        return render_template('trend.html', graph=img_base64, totals=totals, range_selected=range_param)

    except Exception as e:
        return f"<h1>Error in /trend route:</h1><pre>{e}</pre>", 500
@app.route('/export')
def export_trend():
    from flask import request, Response

    range_param = request.args.get('range', '7d')
    now = pd.Timestamp.now()

    if range_param == '24h':
        cutoff = now - pd.Timedelta(hours=24)
    elif range_param == '30d':
        cutoff = now - pd.Timedelta(days=30)
    else:
        cutoff = now - pd.Timedelta(days=7)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_event/<event_type>')
def log_and_notify(event_type):
    log_event(event_type)
    play_sound()
    show_popup("Care Alert", f"Event triggered: {event_type}")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

