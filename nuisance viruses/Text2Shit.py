import keyboard
import random
import string
import time

# Function to scramble text as the user types
def scramble_text(input_text):
    scrambled_text = ""
    for char in input_text:
        if random.random() > 0.7:  # 30% chance to replace the character
            scrambled_text += random.choice(string.punctuation + string.ascii_letters + string.digits)
        else:
            scrambled_text += char
    return scrambled_text

# Function to continuously read keyboard input and scramble it
def text_scrambler():
    typed_text = ""
    print("Text Scrambler activated! Start typing:")

    while True:
        if keyboard.is_pressed("Esc"):  # Exit when the Esc key is pressed
            print("\nText Scrambler deactivated.")
            break
        
        event = keyboard.read_event(suppress=True)  # Read key events, suppressing from printing
        if event.event_type == keyboard.KEY_DOWN:  # Only capture key down events
            char = event.name
            
            # Handle Enter key
            if char == "enter":
                typed_text += "\n"  # Add newline for Enter
            # Handle Backspace key
            elif char == "backspace":
                typed_text = typed_text[:-1]  # Remove last character
            # Ignore non-printable keys
            elif len(char) == 1:  # Only printable characters
                typed_text += char
            
            # Scramble the typed text and print it
            scrambled = scramble_text(typed_text)
            print(f"\rScrambled Text: {scrambled}", end="", flush=True)

        time.sleep(0.1)  # Small delay to simulate real-time typing

# Start the text scrambling process
text_scrambler()
                    