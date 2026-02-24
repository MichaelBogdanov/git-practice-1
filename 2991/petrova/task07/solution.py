#!/usr/bin/env python3
"""
Задача 7: Подсчёт частоты символов в файле
Выводит частоту каждого символа с сортировкой по убыванию
"""

import sys
from collections import Counter

def count_characters(text, ignore_case=False):
    """
    Подсчитывает частоту символов в тексте
    
    Аргументы:
        text (str): входной текст
        ignore_case (bool): игнорировать регистр (True/False)
        
    Возвращает:
        Counter: словарь с частотой символов
    """
    if ignore_case:
        text = text.lower()
    
    # Считаем все символы
    return Counter(text)

def print_frequency(counter):
    """
    Выводит частоту символов в отсортированном по убыванию виде
    """
    # Сортируем по убыванию частоты
    sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    print("\nЧастота символов:")
    print("-" * 40)
    print(f"{'Символ':10} | {'Частота':8} | {'Визуализация'}")
    print("-" * 40)
    
    max_count = max(counter.values()) if counter else 1
    
    for char, count in sorted_items:
        # Красивое отображение специальных символов
        if char == ' ':
            display_char = 'ПРОБЕЛ'
        elif char == '\n':
            display_char = '\\n'
        elif char == '\t':
            display_char = '\\t'
        elif char == '\r':
            display_char = '\\r'
        else:
            display_char = f"'{char}'"
        
        # Визуализация (полоска из #)
        bar_length = int((count / max_count) * 20)
        bar = '#' * bar_length
        
        print(f"{display_char:10} | {count:8} | {bar}")

def read_file(filename):
    """Читает содержимое файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f" Ошибка: файл '{filename}' не найден")
        return None
    except Exception as e:
        print(f" Ошибка при чтении файла: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Использование: python solution.py <файл> [--ignore-case]")
        print("\nПараметры:")
        print("  --ignore-case  : игнорировать регистр (А и а - одно и то же)")
        print("\nПримеры:")
        print("  python solution.py test.txt")
        print("  python solution.py test.txt --ignore-case")
        return
    
    filename = sys.argv[1]
    ignore_case = "--ignore-case" in sys.argv
    
    # Читаем файл
    content = read_file(filename)
    if content is None:
        return
    
    print(f"\n Анализ файла: {filename}")
    print(f" Размер файла: {len(content)} символов")
    print(f" Игнорировать регистр: {'Да' if ignore_case else 'Нет'}")
    
    # Подсчитываем частоту
    frequency = count_characters(content, ignore_case)
    
    # Выводим результат
    print_frequency(frequency)
    
    # Дополнительная информация
    print("-" * 40)
    print(f" Всего уникальных символов: {len(frequency)}")
    print(f" Самый частый символ: '{max(frequency.items(), key=lambda x: x[1])[0]}'")
    print(f" Самый редкий символ: '{min(frequency.items(), key=lambda x: x[1])[0]}'")

def test():
    """Функция для тестирования"""
    test_text = "Hello World! Hello World!"
    
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ")
    print("=" * 50)
    
    print("\n1. Тест с учетом регистра:")
    result1 = count_characters(test_text, ignore_case=False)
    print_frequency(result1)
    
    print("\n2. Тест без учета регистра:")
    result2 = count_characters(test_text, ignore_case=True)
    print_frequency(result2)

if __name__ == "__main__":
    # Если передан аргумент --test, запускаем тест
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test()
    else:
        main()