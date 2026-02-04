import tkinter as tk
from tkinter import messagebox

def start_countdown():
    try:
        total_seconds = int(min_entry.get()) * 60 + int(sec_entry.get())
        if total_seconds <= 0:
            raise ValueError("Enter a positive time.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for minutes and seconds.")
        return

    start_button.config(state='disabled')
    min_entry.config(state='readonly')
    sec_entry.config(state='readonly')
    countdown(total_seconds)

def countdown(seconds_left):
    mins, secs = divmod(seconds_left, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}")
    
    if seconds_left > 0:
        root.after(1000, countdown, seconds_left - 1)
    else:
        messagebox.showinfo("Time's up!", "Countdown finished.")
        start_button.config(state='normal')
        min_entry.config(state='normal')
        sec_entry.config(state='normal')

# GUI setup
root = tk.Tk()
root.title("Countdown Stopwatch")

tk.Label(root, text="Minutes:").grid(row=0, column=0)
min_entry = tk.Entry(root, width=5)
min_entry.grid(row=0, column=1)

tk.Label(root, text="Seconds:").grid(row=0, column=2)
sec_entry = tk.Entry(root, width=5)
sec_entry.grid(row=0, column=3)

start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.grid(row=0, column=4, padx=10)

timer_label = tk.Label(root, text="00:00", font=("Helvetica", 24))
timer_label.grid(row=1, column=0, columnspan=5, pady=20)

root.mainloop()
