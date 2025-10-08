💙 Call Button App
A mobile-friendly alert system designed for 1:1 caregiving, replacing traditional nursing home call buttons using a patient’s phone or tablet.

🧠 Features
📱 Four care request buttons in a clean mobile UI

🔔 Audible alerts and system popups on the caregiver’s PC

📊 Event logging to event_log.csv

📈 Trend dashboard with 24h, 7d, 30d filters

⬇️ CSV export for sharing or analysis

🖥️ Local-only access via LAN/Wi-Fi (no cloud, no tracking)

🛠️ Setup Guide
✅ Prerequisites
Python 3.9+

Flask, Pandas, Matplotlib

PC on local network

Phone/tablet for the patient

📦 Installation
bash
git clone https://github.com/captainlinky/Call_Button_App.git
cd Call_Button_App
pip install -r requirements.txt
python app.py
🌐 Accessing the App
Find your PC’s local IP (e.g., 192.168.1.42)

Open http://192.168.1.42:5000 on the patient’s device

Save as a home screen shortcut

📊 Viewing Trends
Visit http://192.168.1.42:5000/trend

View grouped bar charts by event type and time range

Export data as CSV

🔔 What Happens When a Button Is Pressed
Sound plays on caregiver’s PC

System popup shows event type

Event logged to CSV

Appears in /trend dashboard

🧠 Intended Use
Designed for home-based caregiving, not institutions

Helps track care frequency and types

Useful for building routines, identifying patterns, and sharing data with clinicians

🛡️ Security Note
Runs locally with no authentication

Intended for trusted home networks

Lightweight protection (e.g., PIN access) can be added later

