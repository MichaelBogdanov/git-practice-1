from collections import Counter

# Ввод параметров
filename = input("Имя файла: ")
ignore_case = input("Игнорировать регистр? (y/n): ").lower() == 'y'

# Читаем файл
with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

# Игнорируем регистр если нужно
if ignore_case:
    text = text.lower()

# Считаем частоту символов (включая пробелы и переносы строк)
counter = Counter(text)

# Сортируем по убыванию частоты
sorted_chars = sorted(counter.items(), key=lambda x: x[1], reverse=True)

# Выводим результат
print(f"\n--- Частота символов ---")
print(f"Всего символов: {len(text)}")
print(f"Уникальных символов: {len(counter)}\n")

for char, count in sorted_chars:
    # Красивое отображение спецсимволов
    if char == '\n':
        display = '\\n'
    elif char == '\t':
        display = '\\t'
    elif char == ' ':
        display = 'пробел'
    else:
        display = char
    
    percentage = (count / len(text)) * 100
    print(f"'{display}': {count} раз ({percentage:.1f}%)")