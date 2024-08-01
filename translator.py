#!/usr/bin/env python3

import sys
from deep_translator import GoogleTranslator


LANGUAGES = ['ru', 'en']


def translate_text(target_language, text):
    try:
        translator = GoogleTranslator(source='auto', target=target_language)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Ошибка при переводе: {e}"


def main():
    if len(sys.argv) < 3:
        print("Использование: translate <lang> <text>")
        print("Языки для перевода: en (английский), ru (русский)")
        return

    target_language = sys.argv[1]
    text = " ".join(sys.argv[2:])

    if target_language not in LANGUAGES:
        print("Неправильный язык. Доступные языки:", ", ".join(LANGUAGES))
        return

    translated_text = translate_text(target_language, text)
    print(f"Перевод: {translated_text}")


if __name__ == "__main__":
    main()
