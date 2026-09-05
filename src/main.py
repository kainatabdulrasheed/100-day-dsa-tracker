import tkinter as tk
from tracker import load_data, save_data

# Load saved data
data = load_data()

current_day = data["current_day"]
streak = data["streak"]
best_streak = data["best_streak"]

# Main window
window = tk.Tk()
window.title("100-Day DSA Tracker")
window.geometry("400x500")

def complete_today():
    global current_day
    global streak
    global best_streak

    if current_day < 100:
        current_day += 1
        streak += 1

        if streak > best_streak:
            best_streak = streak

        data["current_day"] = current_day
        data["streak"] = streak
        data["best_streak"] = best_streak

        save_data(data)

        day_label.config(text=f"DAY {current_day:02d} / 100")
        streak_label.config(text=f"🔥 STREAK: {streak} DAYS")
        best_label.config(text=f"🏆 BEST: {best_streak} DAYS")
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
progress_label = tk.Label(
    window,
    text="Progress\n░░░░░░░░░░ 0%",
    font=("Arial", 14)
)
progress_label.pack(pady=15)


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
    text="Last 7 Days\n⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜",
    font=("Arial", 14)
)
history_label.pack(pady=15)


# Run the application
window.mainloop()