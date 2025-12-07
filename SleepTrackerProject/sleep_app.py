import tkinter as tk
from tkinter import messagebox
import json
import os
import pickle
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -------------------------
# Load ML model
# -------------------------
with open("sleep_model.pkl", "rb") as f:
    model = pickle.load(f)

# -------------------------
# History File Setup
# -------------------------
HISTORY_FILE = "sleep_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

# -------------------------
# Prediction Function
# -------------------------
def predict_sleep():
    try:
        s_hours = float(entry_sleep.get())
        stress = float(entry_stress.get())
        screen = float(entry_screen.get())
        exercise = float(entry_exercise.get())

        user_data = np.array([[s_hours, stress, screen, exercise]])
        result = model.predict(user_data)[0]

        # Suggestions
        if result < 50:
            suggestion = "Your sleep quality is low. Reduce stress and screen time."
        elif result < 75:
            suggestion = "Your sleep quality is moderate. Improve consistency."
        else:
            suggestion = "Excellent! Your habits look good."

        output_label.config(
            text=f"Sleep Quality Score: {result:.2f}\nSuggestion: {suggestion}"
        )

        # -------------------------
        # Save to history using today's weekday
        # -------------------------
        today = datetime.now().strftime("%a")  # Mon, Tue, Wed...
        history = load_history()
        history[today] = float(result)
        save_history(history)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# -------------------------
# Chart toggle
# -------------------------
chart_window = None

def toggle_chart():
    global chart_window

    if chart_window and tk.Toplevel.winfo_exists(chart_window):
        chart_window.destroy()
        chart_window = None
        return

    # Create new chart window
    chart_window = tk.Toplevel(app)
    chart_window.title("Sleep Trend Chart")
    chart_window.geometry("650x450")

    history = load_history()

    if not history:
        tk.Label(chart_window, text="No data available to display.", font=("Arial", 14)).pack()
        return

    days_order = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days = [d for d in days_order if d in history]
    values = [history[d] for d in days]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(days, values, marker="o", color="#00B7C2", linewidth=2)
    ax.set_title("Weekly Sleep Quality Trend")
    ax.set_ylabel("Sleep Quality Score")
    ax.set_xlabel("Day")
    ax.grid(True, linestyle="--", alpha=0.4)

    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# -------------------------
# Dark / Light Mode Toggle
# -------------------------
dark_mode = False

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    if dark_mode:
        bg = "#1e1e1e"
        fg = "white"
        entry_bg = "#333333"
        button_bg = "#444444"
    else:
        bg = "white"
        fg = "black"
        entry_bg = "#E8FFFF"  # soft cyan tint
        button_bg = "#00B7C2"

    app.config(bg=bg)
    title_label.config(bg=bg, fg=fg)
    output_label.config(bg=bg, fg=fg)

    for w in widgets:
        if isinstance(w, tk.Label):
            w.config(bg=bg, fg=fg)
        elif isinstance(w, tk.Entry):
            w.config(bg=entry_bg, fg="black")
        elif isinstance(w, tk.Button):
            w.config(bg=button_bg, fg="white", activebackground=button_bg)

# -------------------------
# GUI Layout
# -------------------------
app = tk.Tk()
app.title("Enhanced Sleep Tracker")
app.geometry("380x540")

title_label = tk.Label(app, text="Simple Sleep Tracker", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

widgets = []

def add_label(text):
    lbl = tk.Label(app, text=text, font=("Arial", 12))
    lbl.pack()
    widgets.append(lbl)
    return lbl

def add_entry():
    ent = tk.Entry(app, font=("Arial", 12), width=25)
    ent.pack(pady=3)
    widgets.append(ent)
    return ent

entry_sleep_lbl = add_label("Enter Sleep Hours:")
entry_sleep = add_entry()

entry_stress_lbl = add_label("Stress Level (1–10):")
entry_stress = add_entry()

entry_screen_lbl = add_label("Screen Time Before Bed (hours):")
entry_screen = add_entry()

entry_exercise_lbl = add_label("Exercise Minutes:")
entry_exercise = add_entry()

btn_predict = tk.Button(app, text="Predict Sleep Quality", command=predict_sleep, width=22)
btn_predict.pack(pady=8)
widgets.append(btn_predict)

btn_chart = tk.Button(app, text="Show / Hide Chart", command=toggle_chart, width=22)
btn_chart.pack(pady=8)
widgets.append(btn_chart)

btn_theme = tk.Button(app, text="Toggle Dark / Light Mode", command=toggle_theme, width=22)
btn_theme.pack(pady=8)
widgets.append(btn_theme)

output_label = tk.Label(app, text="", font=("Arial", 12))
output_label.pack(pady=10)

apply_theme()
app.mainloop()
