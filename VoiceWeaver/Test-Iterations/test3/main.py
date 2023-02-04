import tkinter as tk
from tkinter import messagebox
import pyttsx3
import pyperclip

#initialize text-to-speech engine
engine = pyttsx3.init()

#function to read clipboard text
def read_clipboard():
    clipboard_text = pyperclip.paste()
    engine.say(clipboard_text)
    engine.runAndWait()

#function to bind play button to spacebar
def bind_play_button(event):
    read_clipboard()

#function to check for new clipboard text
def check_clipboard():
    current_clipboard_text = pyperclip.paste()
    if current_clipboard_text != clipboard_text:
        clipboard_text = current_clipboard_text
        engine.say(clipboard_text)
        engine.runAndWait()
        root.after(1000, check_clipboard)

#function to minimize application to system tray
def minimize_to_tray(event=None):
    root.iconify()

#function to exit application
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

#create tkinter window
root = tk.Tk()
root.title("Clipboard Reader")

#create play button
play_button = tk.Button(root, text="Play", command=read_clipboard)
play_button.pack()

#bind play button to spacebar
root.bind('<space>', bind_play_button)

#check for new clipboard text every second
check_clipboard()

#create system tray icon
root.withdraw()
root.iconify()
root.update()

#bind minimize to tray
root.bind('<Unmap>', minimize_to_tray)

#exit application on close
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()