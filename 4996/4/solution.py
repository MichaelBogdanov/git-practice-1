# Задача 4: Удаление дубликатов, сохраняя порядок

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

def remove_duplicates(items):
    seen = set()
    result = []
    
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

print("=" * 50)
print("Задача 4: Удаление дубликатов")
print("=" * 50)

input_file = input("Введите имя входного файла: ").strip()
output_file = input("Введите имя выходного файла: ").strip()

content = read_file(input_file)
if content:
    items = content.strip().split()
    
    print(f"Исходные данные ({len(items)} элементов):")
    print(' '.join(items))
    
    unique = remove_duplicates(items)
    
    print(f"После удаления дубликатов ({len(unique)} элементов):")
    result_str = ' '.join(unique)
    print(result_str)
    
    if write_file(output_file, result_str):
        print(f"Сохранено в {output_file}")