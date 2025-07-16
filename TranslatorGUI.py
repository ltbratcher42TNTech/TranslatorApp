import tkinter as tk
from tkinter import ttk

# Initializing Main Window
root = tk.Tk()
root.title("TJ's Translator App")
root.geometry("400x400")
root.resizable(False, False)

# Creating The Text Input Area
tk.Label(root, text="Enter text:").pack(pady=5)
text_input = tk.Text(root, height=5, width=50)
text_input.pack()

# Creating Language Dropdown Selection


root.mainloop()