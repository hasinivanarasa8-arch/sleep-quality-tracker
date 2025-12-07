# 🌙 Sleep Quality Tracker (ML + Tkinter GUI)

A clean, minimalistic, beginner‑friendly yet professional *Sleep Tracking Desktop App* built using:

- *Python*
- *Tkinter (Custom Themed UI)*
- *Matplotlib (Optional Charts)*
- *Pickle‑based ML Model*
- *Local JSON Storage for History*

The app predicts *Sleep Quality Score, stores daily data, and visualizes your weekly progress — with **Dark Mode*, rounded buttons, and smooth nonchalant styling.

## 🚀 Features

### ✔ Machine Learning Prediction  
Predicts sleep quality based on:  
- Sleep Hours  
- Stress Level  
- Screen Time  
- Exercise Minutes  

### ✔ Dark Mode Toggle  
Switch themes instantly.

### ✔ Weekly Graphs  
- Shows only days with real entered data  
- Missing days remain *blank*  
- Toggle graph visibility with one button  

### ✔ Local History  
Each prediction is saved to:

sleep_history.json

Meaning your data stays on your device.

## 📁 Project Structure

📦 SleepTracker ┣ 📜 app.py ┣ 📜 sleep_model.pkl ┣ 📜 sleep_history.json  (auto created)┣ 📜 sleep_model.py ┗ 📜 README.md


## 🛠 Installation & Setup

### *1️⃣ Install Requirements*
```bash
pip install numpy matplotlib

2️⃣ Place Your Model

Make sure this file exists:

sleep_model.pkl

3️⃣ Run the App

python app.py


📸 Screenshots 

1. Home Screen – Light Mode

<img width="475" height="708" alt="image" src="https://github.com/user-attachments/assets/d83b5250-f6a8-4b19-bae4-f8d0a5ad2e9e" />


2. Home Screen – Dark Mode

<img width="465" height="702" alt="image" src="https://github.com/user-attachments/assets/35d58336-1288-4705-9f68-998070a5e24a" />


3. Prediction Output

<img width="651" height="703" alt="image" src="https://github.com/user-attachments/assets/c970a2fd-0766-43c5-9576-253d4871495b" />


4. Weekly Graph Closed

5. Weekly Graph Opened With Data


6. Example Error Handling (Invalid Input)

<img width="657" height="700" alt="image" src="https://github.com/user-attachments/assets/c707c981-87aa-4600-8874-0de366582d69" />



🧠 How Prediction Works

The ML model takes inputs:

[ sleep_hours, stress_level, screen_time, exercise_minutes ]

And outputs a sleep score (0–100).

---
