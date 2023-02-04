import tkinter as tk
from tkinter import ttk
import pyttsx3
import clipboard

class App:
    def __init__(self, master):
        self.master = master
        self.engine = pyttsx3.init()

        # create text editor style window to display clipboard text
        self.text_editor = tk.Text(self.master, state="disabled")
        self.text_editor.pack()

        # bind spacebar key to play/pause voice
        self.master.bind("<space>", self.play_pause_voice)

        # get clipboard text and display in text editor window
        clipboard_text = clipboard.paste()
        self.text_editor.configure(state="normal")
        self.text_editor.insert("end", clipboard_text)
        self.text_editor.configure(state="disabled")

    def play_pause_voice(self, event):
        if self.engine.isBusy():
            self.engine.stop()
        else:
            self.engine.say(self.text_editor.get("1.0", "end-1c"))
            self.engine.startLoop()

root = tk.Tk()
app = App(root)
root.mainloop()
