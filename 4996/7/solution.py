# Задача 7: Подсчёт частоты символов

from collections import Counter

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
        return None

def count_characters(text, ignore_case=False):
    if ignore_case:
        text = text.lower()
    
    counter = Counter(text)
    sorted_chars = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_chars

print("=" * 50)
print("Задача 7: Подсчёт частоты символов")
print("=" * 50)

filename = input("Введите имя файла: ").strip()
ignore = input("Игнорировать регистр? (да/нет): ").strip().lower()
ignore_case = ignore in ['да', 'yes', 'y', 'д']

content = read_file(filename)
if content:
    print(f"\nТекст для анализа:")
    print(content[:200] + "..." if len(content) > 200 else content)
    
    result = count_characters(content, ignore_case)
    
    print(f"\nЧастота символов (всего символов: {len(content)}):")
    print("-" * 30)
    
    for char, count in result:
        if char == '\n':
            char_name = 'новая строка'
        elif char == ' ':
            char_name = 'пробел'
        elif char == '\t':
            char_name = 'табуляция'
        else:
            char_name = char
        
        percentage = (count / len(content)) * 100
        print(f"'{char_name}': {count} раз ({percentage:.1f}%)")