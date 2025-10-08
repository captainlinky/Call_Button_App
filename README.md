
---

```markdown
# 💙 Caregiver Alert Panel

A lightweight, mobile-friendly alert system for **1:1 caregiving**. Designed to replace traditional call buttons with a discreet, emotionally safe interface that runs locally on a patient’s phone or tablet.

---

## 🧠 Features

- 🖱️ Four customizable care request buttons with clear icons  
- 🔔 Audible alerts and system popups on the caregiver’s PC  
- 📊 Event logging to `event_log.csv` for tracking and analysis  
- 📈 `/trend` dashboard with 24h, 7d, and 30d filters  
- ⬇️ CSV export for clinician sharing or personal review  
- 🖥️ Local-only access via LAN/Wi-Fi — **no cloud, no tracking**

---

## 🛠️ Setup Instructions

### ✅ Requirements

- Python 3.9+
- Flask, Pandas, Matplotlib
- PC and mobile device on the same local network

### 📦 Installation

```bash
git clone https://github.com/captainlinky/Call_Button_App.git
cd Call_Button_App
pip install -r requirements.txt
python app.py
```

---

## 🌐 Accessing the Panel

1. Find your PC’s local IP (e.g., `192.168.1.42`)
2. Open `http://192.168.1.42:5000` on the patient’s device
3. Save as a home screen shortcut for easy access

---

## 📊 Viewing Trends

- Navigate to `http://<your-ip>:5000/trend`
- View grouped bar charts by event type and time range
- Export logs as CSV for external use

---

## 🔔 What Happens When a Button Is Pressed

- Sound plays on caregiver’s PC  
- System popup shows the request type  
- Event is logged to `event_log.csv`  
- Appears in the `/trend` dashboard

---

## 🧠 Use Case

Built for **home-based caregiving**, especially in contexts where emotional safety, discretion, and routine tracking matter. Ideal for:

- Monitoring care frequency
- Supporting clinician conversations
- Building adaptive care routines

---

## 🛡️ Security Notes

- Runs locally with **no authentication**  
- Intended for **trusted home networks**  
- PIN protection or lightweight auth can be added if needed

---

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to modify.

---

## Screenshots

<img width="1170" height="2532" alt="image" src="https://github.com/user-attachments/assets/67253283-1946-4f2a-97c2-1d25f9ccda51" />
<img width="835" height="256" alt="image" src="https://github.com/user-attachments/assets/8891446d-bfeb-439e-a05d-b8f5b4c068e4" />
<img width="1170" height="2532" alt="image" src="https://github.com/user-attachments/assets/65c271d7-02f1-4f40-bfc1-401df06f1357" />
```
