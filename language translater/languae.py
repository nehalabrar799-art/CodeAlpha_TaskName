import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3
import pyperclip

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Language mappings supported by GoogleTranslator
lang_codes = {
    "English": "en", "French": "fr", "Spanish": "es", "German": "de", "Hindi": "hi",
    "Arabic": "ar", "Chinese (Simplified)": "zh-CN", "Russian": "ru", "Portuguese": "pt",
    "Japanese": "ja", "Korean": "ko", "Italian": "it", "Dutch": "nl", "Greek": "el",
    "Turkish": "tr", "Urdu": "ur", "Vietnamese": "vi", "Swedish": "sv", "Polish": "pl",
    "Romanian": "ro", "Ukrainian": "uk", "Bengali": "bn", "Gujarati": "gu", "Tamil": "ta",
    "Telugu": "te", "Kannada": "kn", "Marathi": "mr", "Malayalam": "ml"
}

language_list = sorted(lang_codes.keys())

# Functions
def translate_text():
    try:
        src = lang_codes[source_lang.get()]
        tgt = lang_codes[target_lang.get()]
        text = source_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Empty Input", "Please enter text to translate.")
            return

        translate_btn.config(state="disabled")
        translated = GoogleTranslator(source=src, target=tgt).translate(text)
        translated_text.config(state="normal")
        translated_text.delete("1.0", tk.END)
        translated_text.insert(tk.END, translated)
        translated_text.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))
    finally:
        translate_btn.config(state="normal")

def copy_text():
    result = translated_text.get("1.0", tk.END).strip()
    if result:
        pyperclip.copy(result)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

def speak_text():
    result = translated_text.get("1.0", tk.END).strip()
    if result:
        engine.say(result)
        engine.runAndWait()

def clear_text():
    source_text.delete("1.0", tk.END)
    translated_text.config(state="normal")
    translated_text.delete("1.0", tk.END)
    translated_text.config(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("640x560")
root.resizable(False, False)
root.configure(bg="#e6f2ff")

# Title
tk.Label(root, text="🌐 Language Translator", font=("Helvetica", 20, "bold"), bg="#e6f2ff", fg="#004080").pack(pady=15)

# Language selection
frame1 = tk.Frame(root, bg="#e6f2ff")
frame1.pack(pady=5)

tk.Label(frame1, text="From:", font=("Helvetica", 12), bg="#e6f2ff").grid(row=0, column=0)
source_lang = ttk.Combobox(frame1, values=language_list, state='readonly', width=25)
source_lang.set("English")
source_lang.grid(row=0, column=1, padx=10)

tk.Label(frame1, text="To:", font=("Helvetica", 12), bg="#e6f2ff").grid(row=0, column=2)
target_lang = ttk.Combobox(frame1, values=language_list, state='readonly', width=25)
target_lang.set("French")
target_lang.grid(row=0, column=3, padx=10)

# Source text input
tk.Label(root, text="Enter text:", font=("Helvetica", 13), bg="#e6f2ff").pack()
source_text = tk.Text(root, height=6, width=75, font=("Helvetica", 11))
source_text.pack(pady=5)

# Translate button
translate_btn = tk.Button(root, text="Translate", command=translate_text, bg="#66b3ff", fg="white",
                          font=("Helvetica", 13, "bold"), width=20)
translate_btn.pack(pady=10)

# Translated output
tk.Label(root, text="Translated text:", font=("Helvetica", 13), bg="#e6f2ff").pack()
translated_text = tk.Text(root, height=6, width=75, font=("Helvetica", 11), state="disabled", bg="#f0f0f0")
translated_text.pack(pady=5)

# Bottom buttons
frame2 = tk.Frame(root, bg="#e6f2ff")
frame2.pack(pady=15)

tk.Button(frame2, text="📋 Copy", command=copy_text, width=15, bg="#cce6ff", font=("Helvetica", 11)).grid(row=0, column=0, padx=10)
tk.Button(frame2, text="🔊 Speak", command=speak_text, width=15, bg="#cce6ff", font=("Helvetica", 11)).grid(row=0, column=1, padx=10)
tk.Button(frame2, text="🧹 Clear", command=clear_text, width=15, bg="#cce6ff", font=("Helvetica", 11)).grid(row=0, column=2, padx=10)

# Run
root.mainloop()
