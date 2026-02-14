
filename = input("Введите имя файла: ")
try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip()
    
    elements = content.split()
    
    unique_elements = []
    for element in elements:
        if element not in unique_elements:
            unique_elements.append(element)
    
    print("Уникальные элементы в порядке появления:")
    print(' '.join(unique_elements))
    
except FileNotFoundError:
    print(f"Файл '{filename}' не найден!")
except Exception as e:
    print(f"Ошибка: {e}")
