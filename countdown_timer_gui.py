import tkinter as tk
from tkinter import ttk
import time
import threading
import winsound  # Note: This works on Windows for sound alerts

# Define the countdown function
def countdown(t, label, progress_bar):
    original_t = t
    while t and not stop_event.is_set():
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        progress_bar['value'] = ((original_t - t) / original_t) * 100
        time.sleep(1)
        t -= 1
    if not stop_event.is_set():
        label.config(text="Time's up!!")
        winsound.Beep(1000, 1000)  # Frequency 1000 Hz, Duration 1000 ms

def start_countdown():
    global stop_event
    stop_event.clear()
    t = int(entry.get())
    countdown_thread = threading.Thread(target=countdown, args=(t, timer_label, progress_bar))
    countdown_thread.start()

def pause_countdown():
    global stop_event
    stop_event.set()

def reset_countdown():
    global stop_event
    stop_event.set()
    timer_label.config(text="00:00")
    progress_bar['value'] = 0

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Create and place the widgets
entry_label = ttk.Label(root, text="Enter the time in seconds:")
entry_label.pack()

entry = ttk.Entry(root)
entry.pack()

start_button = ttk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack()

pause_button = ttk.Button(root, text="Pause Countdown", command=pause_countdown)
pause_button.pack()

reset_button = ttk.Button(root, text="Reset Countdown", command=reset_countdown)
reset_button.pack()

timer_label = ttk.Label(root, text="00:00", font=('Helvetica', 48))
timer_label.pack()

progress_bar = ttk.Progressbar(root, length=200, mode='determinate')
progress_bar.pack()

# Stop event for threading control
stop_event = threading.Event()

# Run the application
root.mainloop()
