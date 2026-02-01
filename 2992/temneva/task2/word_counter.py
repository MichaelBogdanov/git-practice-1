# 2) Подсчёт слов
# Цель: подсчитать строки, слова и найти самое длинное слово в тексте
# Требования:
# Считать файл
# Отделять слова по пробельным символам и пунктуации
# Вернуть количество строк, слов, самое длинное слово (и его длину)

import sys
import re

def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # разделение на строки и удаление пустых
        lines = content.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        line_count = len(non_empty_lines)
        
        # все слова (буквы, цифры, дефисы внутри слов)
        words = re.findall(r'\b[\w-]+\b', content)
        word_count = len(words)
        
        # самое длинное слово
        if words:
            longest_word = max(words, key=len)
            longest_length = len(longest_word)
        else:
            longest_word = ""
            longest_length = 0
        
        print(f"Файл: {filename}")
        print(f"Строк: {line_count}")
        print(f"Слов: {word_count}")
        
        if word_count > 0:
            print(f"Самое длинное слово: '{longest_word}'")
            print(f"Длина самого длинного слова: {longest_length} символов")

    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    
    filename = sys.argv[1]
    count_words(filename)

if __name__ == "__main__":
    main()