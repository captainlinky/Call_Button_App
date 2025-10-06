This application is designed to replace a traditional nursing home call button using the patient’s cell phone or tablet.

The system runs on a designated “nursing station”—a PC located wherever you typically sit during the day. Once launched, the nursing station begins listening at http://{NURSINGSTATIONIPADDRESS}:5000, making it instantly accessible to any device on your LAN or Wi-Fi network, provided there are no firewalls between the PC and the wireless network.

On the patient’s device, the app can be saved as a home screen shortcut. It opens in a mobile-friendly layout with four clearly labeled buttons:

Urination

Bowel Movement

Food or Drink

General Call

Each button press is timestamped, categorized, and logged to event_log.csv. These events can be visualized at http://{NURSINGSTATIONIPADDRESS}:5000/trend, or by tapping the discreet fifth button at the bottom of the main screen.

When a call is made, the nursing station emits an audible alert and displays a system message indicating the nature of the request.

Note: This application is intended for 1:1 care. It’s built for caregivers supporting loved ones at home, offering a simple way to track care frequency and types—especially useful for identifying patterns, building routines, or sharing data with in-home care staff for diagnostic insight.

<img width="1170" height="2532" alt="image" src="https://github.com/user-attachments/assets/8a96de4a-c92b-43d3-8db3-3b40d704cfc9" /><img width="1170" height="2532" alt="image" src="https://github.com/user-attachments/assets/6e2517b0-b65f-45d1-8166-b345c192bdc8" />

<img width="835" height="256" alt="image" src="https://github.com/user-attachments/assets/0db7359e-b009-44cf-9061-a7f2810d4e95" />
