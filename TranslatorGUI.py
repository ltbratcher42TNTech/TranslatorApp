import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator
import pyperclip

# Defining the languages
LANGUAGES = ['Korean', 'German', 'Spanish']

# Mapping languages
LANGUAGE_MAPPING = {
    'Korean': 'ko',
    'German': 'de',
    'Spanish': 'es'
}

# Defining the translate function
def translate_text():
    input_text = text_input.get("1.0", tk.END)
    selected_language = language_var.get()
    target_lang_code = LANGUAGE_MAPPING.get(selected_language)

    if input_text:
        try:
            translated = GoogleTranslator(source='auto', target=target_lang_code).translate(input_text)
            result_box.config(state='normal')
            result_box.delete("1.0", tk.END)
            result_box.insert(tk.END, translated)
            result_box.config(state='disabled')
        except Exception as e:
            result_box.config(state='normal')
            result_box.delete("1.0", tk.END)
            result_box.insert(tk.END, f"Error: {e}")
            result_box.config(state='disabled')

def copy_to_clipboard():
    translated_text =  result_box.get("1.0", tk.END)
    if translated_text:
        pyperclip.copy(translated_text)

# Initialize the main window
root = tk.Tk()
root.title("TJ's Translator App")
root.geometry("400x400")
root.resizable(False, False)

# Text input area
tk.Label(root, text="Enter text:").pack(pady=5)
text_input = tk.Text(root, height=5, width=50)
text_input.pack()

# Language dropdown
tk.Label(root, text="Select a language:").pack(pady=5)
language_var = tk.StringVar()
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=LANGUAGES, state="readonly")
language_dropdown.current(0)
language_dropdown.pack()

# Translate button
translate_btn = tk.Button(root, text="Translate", command=translate_text)
translate_btn.pack(pady=10)

# Copy tp clipboard button
copy_btn = tk.Button(root, text="Copy Translated Text", command=copy_to_clipboard)
copy_btn.pack(pady=5)


# Translated text output
tk.Label(root, text="Translated text:").pack(pady=5)
result_box = tk.Text(root, height=5, width=50, state='disabled')
result_box.pack()

root.mainloop()
