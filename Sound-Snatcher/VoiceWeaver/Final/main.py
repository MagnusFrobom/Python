import pyttsx3
import tkinter as tk
from pynput import keyboard


class App:
    def __init__(self, root):
        self.root = root
        self.engine = pyttsx3.init()

        # Set up the volume slider
        self.volume = tk.Scale(root, from_=0, to=1, resolution=0.1,
                               orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume.pack()

        # Set up the binding button
        self.bind_button = tk.Button(
            root, text="Change Binding", command=self.change_binding)
        self.bind_button.pack()

        self.is_playing = False
        self.binding_key = None
        self.bind_listener = keyboard.Listener(on_press=self.on_press)
        self.bind_listener.start()

    def toggle(self):
        if self.is_playing:
            self.pause()
        else:
            self.play()

    def play(self):
        self.engine.say(self.get_clipboard_text())
        self.engine.runAndWait()
        self.is_playing = True

    def pause(self):
        self.engine.stop()
        self.is_playing = False

    def set_volume(self, value):
        value = float(value)
        self.engine.setProperty('volume', value)

    def get_clipboard_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(
            self.root.selection_get(selection='CLIPBOARD'))
        return self.root.clipboard_get()

    def change_binding(self):
        self.binding_key = None
        self.bind_button["text"] = "Press a key to bind"

    def on_press(self, key):
        if self.binding_key is None:
            self.binding_key = key
            self.bind_button["text"] = f"Bound to {key}"



root = tk.Tk()
app = App(root)
root.mainloop()
