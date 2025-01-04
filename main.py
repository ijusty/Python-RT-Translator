import pyperclip
import keyboard
import time
from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import simpledialog, messagebox

def translate_text(text, source_language='auto', target_language='en'):
    try:
        # Перевод текста
        translated = GoogleTranslator(source=source_language, target=target_language).translate(text)
        return translated
    except Exception as e:
        print("Error during translation:", e)
        return text 

def on_copy(source_language, target_language):
    time.sleep(0.1)
    text = pyperclip.paste()
    
    if text:
        translated_text = translate_text(text, source_language, target_language)
        pyperclip.copy(translated_text)
        print("Translated text copied to clipboard:", translated_text)
        
        keyboard.press_and_release('ctrl+v')

def start_translator():
    root = tk.Tk()
    root.withdraw() 

    source_language = simpledialog.askstring("Выбор языка", "Введите код языка, с которого переводить (например, 'ru'):")
    target_language = simpledialog.askstring("Выбор языка", "Введите код языка, на который переводить (например, 'en'):")


    main_window = tk.Tk()
    main_window.title("Переводчик")
    main_window.iconbitmap('')

    keyboard.add_hotkey('ctrl+c', lambda: on_copy(source_language, target_language))

    print("Press Ctrl+C to translate selected text...")
    keyboard.wait()
    main_window.mainloop()

if __name__ == "__main__":
    start_translator()
