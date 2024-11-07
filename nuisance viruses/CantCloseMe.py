import tkinter as tk

def unclosable_window():
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Unclosable Window")
    label = tk.Label(root, text="You cannot close this window.", font=("Arial", 16))
    label.pack(padx=20, pady=20)
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button
    root.mainloop()

unclosable_window()
