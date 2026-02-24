#!/usr/bin/env python3
"""
Задача 3: Переворот слов в тексте
Переворачивает порядок слов, удаляя лишние пробелы
"""

import sys
import re

def reverse_words(text):
    """
    Переворачивает порядок слов в тексте
    
    Аргументы:
        text (str): входной текст
        
    Возвращает:
        str: текст с перевернутым порядком слов
    """
    # Удаляем пробелы в начале и конце, заменяем несколько пробелов на один
    text = ' '.join(text.split())
    
    # Разбиваем на слова
    words = text.split()
    
    # Переворачиваем порядок слов
    reversed_words = words[::-1]
    
    # Соединяем обратно с одним пробелом
    return ' '.join(reversed_words)

def read_file(filename):
    """Читает содержимое файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

def write_file(filename, content):
    """Записывает содержимое в файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Использование: python solution.py <входной_файл> [выходной_файл]")
        print("Пример: python solution.py input.txt output.txt")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Читаем входной файл
    content = read_file(input_file)
    if content is None:
        return
    
    print(f"Исходный текст: '{content}'")
    
    # Переворачиваем слова
    result = reverse_words(content)
    
    print(f"Результат: '{result}'")
    
    # Сохраняем или выводим результат
    if output_file:
        if write_file(output_file, result):
            print(f"Результат сохранен в файл: {output_file}")
    else:
        print(f"\nРезультат:\n{result}")

if __name__ == "__main__":
    main()