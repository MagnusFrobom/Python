import pyttsx3
import win32clipboard

def read_clipboard():
    # Get the clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Speak the clipboard data
    engine.say(data)
    engine.runAndWait()

# Create the GUI
# This example uses the tkinter library, which is included with Python
from tkinter import *

root = Tk()

# Create a button that will run the read_clipboard function when clicked
button = Button(root, text="Read Clipboard", command=read_clipboard)
button.pack()

root.mainloop()