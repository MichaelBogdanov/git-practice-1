# Задача 3: Переворот слов в тексте
# Переворачивает порядок слов, сохраняя слова как блоки

import re

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
        return None

def write_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Ошибка при записи: {e}")
        return False

def reverse_words(text):
    if not text:
        return ""
    
    # Находим все слова
    words = re.findall(r"[a-zA-Zа-яА-Я0-9]+", text)
    # Находим все разделители
    delimiters = re.split(r"[a-zA-Zа-яА-Я0-9]+", text)
    
    # Переворачиваем слова
    reversed_words = list(reversed(words))
    
    # Собираем результат
    result = []
    for i in range(len(delimiters) - 1):
        result.append(delimiters[i])
        if i < len(reversed_words):
            result.append(reversed_words[i])
    
    if len(delimiters) > len(result) // 2 + 1:
        result.append(delimiters[-1])
    
    # Нормализуем пробелы
    result_text = ''.join(result)
    result_text = re.sub(r' +', ' ', result_text).strip()
    
    return result_text

print("=" * 50)
print("Задача 3: Переворот слов в тексте")
print("=" * 50)

input_file = input("Введите имя входного файла: ").strip()
output_file = input("Введите имя выходного файла: ").strip()

content = read_file(input_file)
if content:
    print(f"\nИсходный текст:")
    print(content)
    
    result = reverse_words(content)
    
    print(f"\nРезультат:")
    print(result)
    
    if write_file(output_file, result):
        print(f"\nСохранено в {output_file}")