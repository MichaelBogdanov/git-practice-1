import re
import sys

def analyze_text(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return

    line_count = len(lines)
    word_count = 0
    longest_word = ""

    # Регулярное выражение: разделяет по любым символам, кроме букв и цифр
    pattern = re.compile(r'[^\w]+') 

    for line in lines:
        # Разбиваем строку, отбрасываем пустые строки
        words = [w for w in pattern.split(line) if w]
        word_count += len(words)
        
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

    print(f"Количество строк: {line_count}")
    print(f"Количество слов: {word_count}")
    print(f"Самое длинное слово: '{longest_word}' (длина: {len(longest_word)})")

if __name__ == "__main__":
    # Если имя файла передано при запуске (например: python solution.py input.txt)
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    # Если запустили просто python solution.py, спрашиваем вручную
    else:
        file_name = input("Введите имя текстового файла (например, input.txt): ")
        
    analyze_text(file_name)