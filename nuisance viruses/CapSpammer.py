import keyboard
import random
import time

# Function to toggle Caps Lock
def toggle_caps_lock():
    # Simulate pressing the Caps Lock key
    keyboard.press_and_release('caps lock')

# Function to run the Caps Lock Toggle virus
def caps_lock_toggle_virus():
    print("Caps Lock Toggle Virus activated!")
    print("Caps Lock will be toggled randomly. Press 'Esc' to stop.")
    
    while True:
        if keyboard.is_pressed('Esc'):  # Exit when the 'Esc' key is pressed
            print("\nCaps Lock Toggle Virus deactivated.")
            break
        
        # Randomly toggle the Caps Lock every 1 to 5 seconds
        toggle_caps_lock()
        toggle_interval = random.randint(1, 5)  # Random interval between 1 and 5 seconds
        time.sleep(toggle_interval)  # Wait for the next toggle

# Start the Caps Lock Toggle virus
caps_lock_toggle_virus()
