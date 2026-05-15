# Задача 2: Подсчёт слов
# Подсчитывает строки, слова и находит самое длинное слово

import re

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
        return None

def split_into_words(text):
    words = re.findall(r"[a-zA-Zа-яА-Я0-9]+", text)
    return words

def analyze_text(text):
    if not text:
        return 0, 0, None, 0
    
    lines = text.splitlines()
    line_count = len(lines)
    
    words = split_into_words(text)
    word_count = len(words)
    
    longest_word = None
    longest_length = 0
    
    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_word = word
    
    return line_count, word_count, longest_word, longest_length

print("=" * 50)
print("Задача 2: Подсчёт слов")
print("=" * 50)

filename = input("Введите имя файла: ").strip()

content = read_file(filename)
if content:
    lines, words, longest_word, longest_len = analyze_text(content)
    
    print("\nРезультаты анализа:")
    print(f"Количество строк: {lines}")
    print(f"Количество слов: {words}")
    print(f"Самое длинное слово: '{longest_word}'")
    print(f"Длина: {longest_len}")