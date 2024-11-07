import tkinter as tk
import random
import pygame
import numpy as np

# Initialize pygame mixer for sound
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.title("FlickerFury")

# Set the window to full screen
root.attributes('-fullscreen', True)

# Create a label to display the mocking text
label = tk.Label(root, font=('Helvetica', 30, 'bold'), fg='white', bg='black', text="YOU'RE DOING IT WRONG!")
label.place(x=0, y=0)

# List of mocking messages
messages = [
    "IS THIS REALLY NECESSARY?",
    "YOU CAN'T ESCAPE ME!",
    "YOU'RE JUST HELPING ME EXPAND.",
    "STOP TRYING TO CLOSE ME!",
    "YOU’RE A BRAVE ONE, AREN’T YOU?",
    "CLICK ALL YOU WANT, NOTHING WILL STOP ME!",
    "DOES THIS MAKE YOU ANGRY?",
    "MY FLICKERING WILL DRIVE YOU CRAZY!",
    "HAHA, I CAN'T BE UNINSTALLED!",
    "YOU THINK ESC WILL WORK? THINK AGAIN!"
]

# Function to generate beep sound
def generate_beep(frequency=1000, duration=200):
    sample_rate = 44100  # samples per second
    t = np.linspace(0, duration / 1000.0, int(sample_rate * (duration / 1000.0)))
    sound = np.sin(2 * np.pi * frequency * t) * 32767  # sine wave
    sound = sound.astype(np.int16)  # convert to 16-bit PCM format
    pygame.mixer.Sound(buffer=sound).play()

# Define the flickering function
def flicker():
    # Ensure the window size is updated
    root.update_idletasks()
    
    # Get the window width and height
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Randomly select a color for the background
    color = random.choice(["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFFFFF", "#000000"])
    
    # Change the background color of the window
    root.config(bg=color)
    
    # Randomly change the text color and message
    label.config(fg=random.choice(["#FFFFFF", "#FF0000", "#FFFF00", "#00FF00", "#FF00FF"]))
    label.config(text=random.choice(messages))
    
    # Position the text randomly on the screen
    label.place(x=random.randint(0, window_width - 300), y=random.randint(0, window_height - 100))
    
    # Play a random sound (beep or buzz)
    generate_beep(frequency=random.randint(500, 2000), duration=random.randint(100, 400))
    
    # Call this function again after a random delay (between 50 and 150 milliseconds)
    root.after(random.randint(50, 150), flicker)

# Start the flickering effect
flicker()

# Start the tkinter main loop
root.mainloop()
