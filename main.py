import pyperclip
import keyboard
import time
from deep_translator import GoogleTranslator

def translate_text(text, source_language='auto', target_language='en'):
    try:
        translated = GoogleTranslator(source=source_language, target=target_language).translate(text)
        return translated
    except Exception as e:
        print("Ошибка при переводе:", e)
        return text

def on_copy(source_language, target_language):
    text = pyperclip.paste()
    print("Текст для перевода: ", text)
    if text:
        translated_text = translate_text(text, source_language, target_language)
        pyperclip.copy(translated_text)
        print("Переведенный текст:", translated_text)
        keyboard.press_and_release('ctrl+v')

def start_translator():
    source_language = input("Введите код языка, с которого переводить (например, 'ru' для русского): ")
    target_language = input("Введите код языка, на который переводить (например, 'en' для английского): ")

    keyboard.add_hotkey('ctrl+c', lambda: on_copy(source_language, target_language))

    print("Переводчик работает.")
    keyboard.wait()

if __name__ == "__main__":
    start_translator()
