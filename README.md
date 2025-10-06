markdown
# 💙 Call Button App

A simple, mobile-friendly alert system for 1:1 caregiving—built to replace the traditional nursing home call button using a patient’s phone or tablet.

This app helps caregivers track and respond to care needs in real time, while logging events for later review. It’s designed for loved ones caring at home, not institutions.

---

## 🧩 Features

- 📱 Mobile-friendly interface with 4 care request buttons  
- 🔔 Audible alerts and system popups on the caregiver’s PC  
- 🧠 Event logging to `event_log.csv`  
- 📊 Visual trend dashboard with time filters (24h, 7d, 30d)  
- ⬇️ CSV export for sharing or analysis  
- 🖥️ Local-only access via LAN/Wi-Fi—no cloud, no tracking

---

## 🛠️ Setup Guide

### ✅ Prerequisites

- Python 3.9+  
- Flask, Pandas, Matplotlib  
- A PC on your local network  
- A phone or tablet for the patient

### 📦 Installation

Option 1: Clone the repo

```bash
git clone https://github.com/captainlinky/Call_Button_App.git
cd Call_Button_App
Option 2: Download ZIP

Click Code → Download ZIP

Extract and open the folder

📦 Install dependencies
bash
pip install -r requirements.txt
Or manually:

bash
pip install flask pandas matplotlib
🚀 Run the app
bash
python app.py
You’ll see something like:

Code
 * Running on http://127.0.0.1:5000
🌐 Accessing the App
Find your PC’s local IP (e.g., 192.168.1.42) and open:

Code
http://192.168.1.42:5000
On the patient’s phone/tablet, save this as a home screen shortcut. It opens in a clean, mobile-friendly layout.

📊 Viewing Trends
Visit:

Code
http://192.168.1.42:5000/trend
Or tap the “View Event Trends” button at the bottom of the main screen.

You’ll see a grouped bar chart showing event frequency over time, with a dropdown to filter by range. You can also export the data as CSV.

🔔 What Happens When a Button Is Pressed
A sound plays on the caregiver’s PC

A system popup shows the event type

The event is logged to event_log.csv

It appears in the /trend dashboard

🧠 Intended Use
This app is designed for 1:1 caregiving—especially for those supporting loved ones at home. It helps track care frequency and types, which can be useful for:

Building routines

Identifying patterns

Sharing data with in-home care staff or clinicians

It’s not meant for institutional use or multi-patient setups.

🛡️ Security Note
This app runs locally and does not include authentication. It’s intended for trusted home networks. If you need lightweight protection later, options like basic auth or PIN-based access can be added.
