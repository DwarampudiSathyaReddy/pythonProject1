import tkinter as tk
from tkinter import messagebox

def display_message():
    messagebox.showinfo("Message", "Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Program")

# Create a button widget
button = tk.Button(root, text="Click Me", command=display_message)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

