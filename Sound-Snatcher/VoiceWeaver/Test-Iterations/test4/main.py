import pyttsx3
import clipboard

engine = pyttsx3.init()

#get the clipboard text
clipboard_text = clipboard.paste()

#speak the clipboard text
engine.say(clipboard_text)
engine.runAndWait()

#To auto update the text if there's a new clipboard text, you can use a while loop to continuously check for changes in the clipboard:

import pyttsx3
import clipboard

engine = pyttsx3.init()

# get the initial clipboard text
clipboard_text = clipboard.paste()

while True:
    # check for changes in the clipboard text
    new_clipboard_text = clipboard.paste()
    if new_clipboard_text != clipboard_text:
        clipboard_text = new_clipboard_text
        # speak the new clipboard text
        engine.say(clipboard_text)
        engine.runAndWait()

# To add play, pause, and reset buttons that bind to the spacebar, you can use the tkinter library to create the buttons and bind them to the spacebar key:

import pyttsx3
import clipboard
from tkinter import *

# create the tkinter window
root = Tk()

# create the play, pause, and reset buttons
play_button = Button(root, text="Play", command=lambda: engine.startLoop())
pause_button = Button(root, text="Pause", command=lambda: engine.stop())
reset_button = Button(root, text="Reset", command=lambda: engine.reset())

# bind the buttons to the spacebar key
root.bind("<space>", lambda e: engine.startLoop())
root.bind("<space>", lambda e: engine.stop())
root.bind("<space>", lambda e: engine.reset())

# pack the buttons into the tkinter window
play_button.pack()
pause_button.pack()
reset_button.pack()

root.mainloop()

# To minimize the application to the systemtray, you can use the system tray widget provided by the tkinter library:

import pyttsx3
import clipboard
from tkinter import *

# create the tkinter window
root = Tk()

# create the system tray widget
system_tray = SystemTray(root)

# create the play, pause, and reset buttons
play_button = Button(root, text="Play", command=lambda: engine.startLoop())
pause_button = Button(root, text="Pause", command=lambda: engine.stop())
reset_button = Button(root, text="Reset", command=lambda: engine.reset())

# bind the buttons to the spacebar key
root.bind("<space>", lambda e: engine.startLoop())
root.bind("<space>", lambda e: engine.stop())
root.bind("<space>", lambda e: engine.reset())

# pack the buttons into the tkinter window
play_button.pack()
pause_button.pack()
reset_button.pack()

# minimize the window to the system tray
root.wm_withdraw()

root.tk