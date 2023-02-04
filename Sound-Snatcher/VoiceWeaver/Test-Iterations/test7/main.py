import tkinter as tk
from tkinter import *
import clipboard
from pynput import keyboard

# set up system tray icon
root = tk.Tk()
root.withdraw()

# create tray icon
tray_icon = tk.Toplevel(root)
tray_icon.overrideredirect(1)
tray_icon.geometry("+250+250")

# create and set clipboard text variable
clipboard_text = clipboard.paste()
clipboard_label = tk.Label(tray_icon, text=clipboard_text)
clipboard_label.pack()

# create and set up play/pause button
play_pause_button = tk.Button(tray_icon, text="Play/Pause")

# create function to play/pause with spacebar
def on_press(key):
    if key == keyboard.Key.space:
    # play/pause code here
        pass

# create and set up volume slider
volume_slider = tk.Scale(tray_icon, from_=1, to=100, orient=HORIZONTAL)
volume_slider.pack()

# create and set up voice rate slider
voice_rate_slider = tk.Scale(tray_icon, from_=1, to=100, orient=HORIZONTAL)
voice_rate_slider.pack()

# set up listener for spacebar press
listener = keyboard.Listener(on_press=on_press)
listener.start()

# update clipboard text and display in tray icon
def update_clipboard():
    clipboard_text = clipboard.paste()
    clipboard_label.config(text=clipboard_text)
    tray_icon.after(1000, update_clipboard)

update_clipboard()

root.mainloop()