import tkinter as tk
from tkinter import ttk
from datetime import date, timedelta
from tracker import load_data, save_data, get_today

# Load saved data
data = load_data()

current_day = data["current_day"]
streak = data["streak"]
best_streak = data["best_streak"]
today_completed = False

# Main window
window = tk.Tk()
window.title("100-Day DSA Tracker")
window.geometry("400x500")

def update_history_display():
    today = date.today()

    history = data["history"]

    symbols = []

    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        day_string = str(day)

        if day_string in history:
            symbols.append("✅")
        else:
            symbols.append("⬜")

    history_label.config(
        text="Last 7 Days\n" + " ".join(symbols)
    )

def calculate_streak():
    today = date.today()

    history = data["history"]

    streak_count = 0
    check_date = today

    while str(check_date) in history:
        streak_count += 1
        check_date -= timedelta(days=1)

    return streak_count

def complete_today():
    global current_day
    global streak
    global best_streak
    global today_completed

    today = get_today()

    if current_day < 100 and not today_completed and today not in data["history"]:
        current_day += 1

        data["history"].append(today)

        streak = calculate_streak()

        if streak > best_streak:
            best_streak = streak

        data["current_day"] = current_day
        data["streak"] = streak
        data["best_streak"] = best_streak

        save_data(data)

        day_label.config(text=f"DAY {current_day:02d} / 100")
        streak_label.config(text=f"🔥 STREAK: {streak} DAYS")
        best_label.config(text=f"🏆 BEST: {best_streak} DAYS")

        progress_text.config(text=f"Progress: {current_day}%")
        progress_bar["value"] = current_day

        update_history_display()

        today_completed = True
        complete_button.config(state="disabled")

# Title
title_label = tk.Label(
    window,
    text="🧠 100-DAY DSA TRACKER",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)


# Day counter
day_label = tk.Label(
    window,
    text=f"DAY {current_day:02d} / 100",
    font=("Arial", 18)
)
day_label.pack(pady=10)


# Current streak
streak_label = tk.Label(
    window,
    text=f"🔥 STREAK: {streak} DAYS",
    font=("Arial", 14)
)
streak_label.pack(pady=5)


# Best streak
best_label = tk.Label(
    window,
    text=f"🏆 BEST: {best_streak} DAYS",
    font=("Arial", 14)
)
best_label.pack(pady=5)


# Progress
progress_text = tk.Label(
    window,
    text=f"Progress: {current_day}%",
    font=("Arial", 14)
)

progress_text.pack(pady=5)


progress_bar = ttk.Progressbar(
    window,
    orient="horizontal",
    length=250,
    mode="determinate",
    maximum=100
)

progress_bar.pack(pady=10)
progress_bar["value"] = current_day

# Complete button
complete_button = tk.Button(
    window,
    text="✅ COMPLETE TODAY",
    font=("Arial", 13, "bold"),
    padx=20,
    pady=10,
    command=complete_today
)
complete_button.pack(pady=15)


# Last 7 days
history_label = tk.Label(
    window,
    font=("Arial", 14)
)

history_label.pack(pady=15)
update_history_display()

# Run the application
window.mainloop()