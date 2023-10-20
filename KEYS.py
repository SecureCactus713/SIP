import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from pynput.keyboard import Listener
import threading
import datetime
import textwrap  # Added import for text wrapping

# Function that will display the key pressed to the GUI
def key_pressed(key):
    if not should_stop():
        key = str(key)
        key = key.replace("'", "")
        text_box1.insert(tk.END, key + ' ')  # Add a space after each key press

# Flag to signal the keylogger thread to stop
keylogger_stopped = threading.Event()

# Function to check if the keylogger should stop
def should_stop():
    return keylogger_stopped.is_set()

# Function that will start the keylogger in a new thread
def start_keylogger_thread():
    keylogger_stopped.clear()
    info_text = "What is a Keylogger? A keylogger program, often simply referred to as a keylogger, is a type of " \
                "software or hardware designed to covertly record the keystrokes of a computer or device's keyboard. " \
                "The primary purpose of a keylogger is to monitor and capture the keys pressed by a user, which can " \
                "include letters, numbers, special characters, and even function keys. " \
                "Keyloggers can be used for legitimate purposes, such as System Monitoring, Parental Control, and " \
                "Data Recovery. However, keyloggers are often associated with malicious intent and are frequently " \
                "used for illegal or unethical activities, such as Identity Theft, Espionage, and Cyberstalking."
    wrapped_text = textwrap.fill(info_text, width=50)  # Wrap the text to fit the width of the text box
    display_info_in_text_box2(wrapped_text)
    t = threading.Thread(target=start_keylogger)
    t.start()
    status_var.set("Keylogger Running")

# Function that will start the keylogger
def start_keylogger():
    with Listener(on_press=key_pressed) as l:
        l.join()

# Function that will stop the keylogger without closing the program
def stop_keylogger():
    keylogger_stopped.set()
    info_text = "How to Protect Against Malicious Keyloggers? Protecting against malicious software is essential to " \
                "safeguard your personal and sensitive information from being stolen. Some effective ways to protect " \
                "yourself against malicious keyloggers are by Using Antivirus and Anti-Malware Software, Keep The " \
                "Operating System and Software Up to Date, Download Software from Trusted Sources, Be Cautious with " \
                "Email Attachments and Links, Use Strong and Unique Passwords, Enable Two-Factor Authentication " \
                "(2FA), Regularly Check for Unwanted Software, and most importantly Educate Yourself. Staying " \
                "informed about the latest security threats and best practices for online safety is the most " \
                "important means to protect yourself. Awareness and knowledge is a powerful tool in preventing " \
                "attacks. And knowing is half the battle."
    wrapped_text = textwrap.fill(info_text, width=50)  # Wrap the text to fit the width of the text box
    display_info_in_text_box2(wrapped_text)
    status_var.set("Keylogger Stopped")

# Function for exporting the captured keystrokes to a log file with date and time in the name
def export_keystrokes():
    content = text_box1.get("1.0", tk.END)
    # Generate the filename with date and time
    now = datetime.datetime.now()
    filename = f"captured_keystrokes_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, "w") as file:
        file.write(content)
    text_box1.delete("1.0", tk.END)  # Clear text_box1 after exporting
    info_text = "How to find and remove an unwanted keylogger. Finding and removing an unwanted keylogger from your " \
                "computer is essential for maintaining your privacy and security. Here are some steps you can take " \
                "to detect and remove keyloggers. Ensure that your antivirus and anti-malware software is up to date " \
                "and run a full system scan to detect and remove any unwanted programs like keyloggers. In addition " \
                "to your antivirus program, consider using specialized anti-malware software like Malwarebytes, " \
                "Spybot Search & Destroy, or HitmanPro. These tools are designed to detect and remove various types " \
                "of malware, including keyloggers. A firewall also can help prevent unauthorized communication " \
                "between your computer and external servers. Configure your firewall to block any suspicious " \
                "outgoing connections. Review the list of installed programs on your computer. Sometimes keyloggers " \
                "may appear as suspicious or unknown software. Uninstall any programs that you don't recognize or " \
                "trust. Check for any suspicious processes or applications. Look for anything unusual or unknown and " \
                "disable any startup items that you don't recognize or that seem suspicious. Keyloggers can " \
                "sometimes be browser extensions or add-ons. Review and disable any suspicious extensions in your " \
                "web browser. Ensure that your operating system and all software are up to date. Security patches " \
                "can fix vulnerabilities that keyloggers might exploit. If you're unable to remove the keylogger or " \
                "have strong reasons to believe that your system is compromised beyond repair, consider consulting a " \
                "professional or an IT expert who can assist in the removal process or consider reinstalling your " \
                "operating system. A reinstall should be a last resort, as it involves wiping your computer clean " \
                "and reinstalling everything. Remember that the best defense against keyloggers is prevention. " \
                "Regularly update your security software, practice safe browsing habits, and be cautious when " \
                "downloading and installing software from the internet."
    wrapped_text = textwrap.fill(info_text, width=50)  # Wrap the text to fit the width of the text box
    display_info_in_text_box2(wrapped_text)

# Function to display info in text_box2
def display_info_in_text_box2(info_text):
    text_box2.delete("1.0", tk.END)
    text_box2.insert(tk.END, info_text)

# Creating the GUI
window = tk.Tk()
window.title("KEYS Learning Software")
window.geometry("1000x600")  # Adjusted window size
window.configure(bg="grey")

# Create a frame for the text boxes and scrollbar
text_box_frame = tk.Frame(window)
text_box_frame.pack(fill=tk.BOTH, expand=True)

# Creating the original text box with a fixed height and a scrollbar
text_box1 = scrolledtext.ScrolledText(text_box_frame, height=15, width=50)  # Adjust the height as needed
text_box1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, side=tk.LEFT)

# Creating the new text box to the right of the original text box with the same fixed height
text_box2 = scrolledtext.ScrolledText(text_box_frame, height=15, width=50)  # Adjust the height as needed
text_box2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, side=tk.RIGHT)

# Create a frame for the buttons and status bar below the text boxes
button_frame = tk.Frame(window)
button_frame.pack(side=tk.BOTTOM, pady=20)

# Creating the button that will start the keylogger
start_button = ttk.Button(button_frame, text="Start Keylogger", command=start_keylogger_thread)
start_button.grid(row=0, column=0, padx=10)

# Creating the button that will stop the keylogger
stop_button = ttk.Button(button_frame, text="Stop Keylogger", command=stop_keylogger)
stop_button.grid(row=0, column=1, padx=10)

# Creating the "Export" button
export_button = ttk.Button(button_frame, text="Export", command=export_keystrokes)
export_button.grid(row=0, column=2, padx=10)

# Creating the status bar
status_var = tk.StringVar()
status_label = tk.Label(button_frame, textvariable=status_var, fg="blue")
status_var.set("Keylogger Stopped")
status_label.grid(row=1, columnspan=3, pady=10)

# Running the GUI
window.mainloop()
