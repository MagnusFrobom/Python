import tkinter as tk
import pyperclip

root = tk.Tk()
root.title("Clipboard Monitor")

# create a label to display the clipboard text
clipboard_label = tk.Label(root, text="")
clipboard_label.pack()

# function to update the clipboard text in the label
def update_clipboard():
    clipboard_text = pyperclip.paste()
    clipboard_label.config(text=clipboard_text)

# set an interval to update the clipboard text
root.after(1000, update_clipboard)

root.mainloop()