import tkinter as tk


# Main window
window = tk.Tk()
window.title("100-Day DSA Tracker")
window.geometry("400x500")

current_day = 0


def complete_today():
    global current_day
    if current_day < 100:
        current_day += 1
        day_label.config(text=f"DAY {current_day:02d} / 100")
        # complete_button.config(state="disabled")
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
    text="DAY 0 / 100",
    font=("Arial", 18)
)
day_label.pack(pady=10)


# Current streak
streak_label = tk.Label(
    window,
    text="🔥 STREAK: 0 DAYS",
    font=("Arial", 14)
)
streak_label.pack(pady=5)


# Best streak
best_label = tk.Label(
    window,
    text="🏆 BEST: 0 DAYS",
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