import pyttsx3
import win32clipboard
import win32con
from tkinter import *

# Initialize pyttsx3
engine = pyttsx3.init()

# Function to read clipboard and speak its contents
def read_clipboard():
    # Get clipboard contents
    win32clipboard.OpenClipboard()
    clipboard_text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

    # Speak clipboard contents
    engine.say(clipboard_text)
    engine.runAndWait()

# Function to update clipboard and speak its contents
def update_clipboard():
    # Update clipboard contents
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text_field.get())
    win32clipboard.CloseClipboard()

    # Speak clipboard contents
    read_clipboard()

# Function to play audio
def play_audio():
    engine.resume()

# Function to pause audio
def pause_audio():
    engine.pause()

# Function to reset audio
def reset_audio():
    engine.stop()

# Function to minimize application to system tray
def minimize_to_tray(root):
    # Hide window
    root.withdraw()

    # Create an icon in the system tray
    hwnd = win32gui.FindWindow(None, "Clipboard Reader")
    win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP, hwnd, win32gui.LoadIcon(0, win32con.IDI_APPLICATION), "Clipboard Reader")

    # Register a WndProc hook to handle messages from the system tray
    win32gui.PumpMessages()

# Create GUI
root = Tk()
root.title("Clipboard Reader")

# Text field to display clipboard contents