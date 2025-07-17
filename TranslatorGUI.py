import tkinter as tk
from tkinter import ttk

LANGUAGES = ['Korean', 'German', 'Spanish']

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
tk.Label(root, text="Select a language:").pack(pady=5)
language_var = tk.StringVar()
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=LANGUAGES, state="readonly")
language_dropdown.current(0)
language_dropdown.pack()

# Translate Button
translate_btn = tk.Button(root, text="Translate")
translate_btn.pack(pady=10)

# Translated Text Output Box
tk.Label(root, text="Translated text:").pack(pady=5)
result_box = tk.Text(root, height=5, width=50, state='normal')
result_box.pack()




root.mainloop()