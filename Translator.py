import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Function to translate text
def translate_text():
    # Get the text to be translated and the selected languages
    text_to_translate = text_input.get("1.0", "end-1c")
    from_lang = from_lang_combobox.get()
    to_lang = to_lang_combobox.get()
    
    # Initialize the Translator
    translator = Translator()
    
    # Translate the text
    translated = translator.translate(text_to_translate, src=from_lang, dest=to_lang)
    
    # Display the translated text
    translated_text.delete("1.0", "end")
    translated_text.insert("1.0", translated.text)

# Create the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")

# Create input text box
text_input_label = tk.Label(root, text="Enter text to translate:")
text_input_label.pack(pady=5)

text_input = tk.Text(root, height=5, width=50)
text_input.pack(pady=5)

# Create language selection boxes
languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'hi', 'ar', 'zh-cn']

from_lang_label = tk.Label(root, text="From Language:")
from_lang_label.pack(pady=5)

from_lang_combobox = ttk.Combobox(root, values=languages, state="readonly")
from_lang_combobox.set('en')  # Default language
from_lang_combobox.pack(pady=5)

to_lang_label = tk.Label(root, text="To Language:")
to_lang_label.pack(pady=5)

to_lang_combobox = ttk.Combobox(root, values=languages, state="readonly")
to_lang_combobox.set('es')  # Default language
to_lang_combobox.pack(pady=5)

# Create a translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Create output text box for translated text
translated_text_label = tk.Label(root, text="Translated Text:")
translated_text_label.pack(pady=5)

translated_text = tk.Text(root, height=5, width=50)
translated_text.pack(pady=5)

# Run the application
root.mainloop()
