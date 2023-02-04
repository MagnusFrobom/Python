import pyttsx3
import win32clipboard
import win32gui
import win32con
import time
import threading

# initializing text-to-speech engine
engine = pyttsx3.init()

# function to read clipboard text
def read_clipboard():
    # access clipboard
    win32clipboard.OpenClipboard()
    # get clipboard text
    text = win32clipboard.GetClipboardData()
    # close clipboard
    win32clipboard.CloseClipboard()
    # return text
    return text

# function to play text-to-speech
def play_text():
    # read clipboard text
    text = read_clipboard()
    # speak text
    engine.say(text)
    engine.runAndWait()

# function to handle key press events
def onKeyboardEvent(event):
    # check if spacebar is pressed
    if event.Ascii == 32:
        # start thread to play text-to-speech
        thread = threading.Thread(target=play_text)
        thread.start()

# create window
wnd = win32gui.CreateWindow(win32con.WS_EX_TOPMOST, win32con.WS_POPUP, 0, 0, 0, 0, 0, 0, 0, None, None)
# set window to be always on top
win32gui.SetWindowPos(wnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
# hide window
win32gui.ShowWindow(wnd, win32con.SW_HIDE)

# create keyboard hook
hm = pyxhook.HookManager()
# set key press event handler
hm.KeyDown = onKeyboardEvent
# start hook
hm.HookKeyboard()

# keep application running
while True:
    time.sleep(0.1)