import pyttsx3
import tkinter as tk

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def on_play_pause():
    # Get a reference to the button widget
    button = on_play_pause.button

    # Get the current text of the button
    text = button['text']

    if text == "Play":
        # Get the text from the clipboard
        text = root.clipboard_get()

        # Set the rate and volume of the speech
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume+0.1)

        # Queue the text for speaking
        engine.say(text)

        # Start the engine
        engine.runAndWait()

        # Update the button text
        button.config(text="Pause")
    else:
        # Stop the engine if it is currently speaking
        engine.stop()

        # Update the button text
        button.config(text="Play")


# Create the main window
root = tk.Tk()
root.title("Text-to-Speech")

# Create the play/pause button
play_pause_button = tk.Button(root, text="Play", command=on_play_pause)

# Save a reference to the button widget in the function
on_play_pause.button = play_pause_button

# Pack the button into the window
play_pause_button.pack()

# Run the Tkinter event loop
root.mainloop()
