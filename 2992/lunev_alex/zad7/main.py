input_file = 'input.txt'
output_file = 'output.txt'

# Игнорировать/Нет (регистр)
ignore_case = True

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if ignore_case:
        text = text.lower()
        print("Регистр игнорируется")
    else:
        print("Регистр учитывается")
    
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Преобразуем словарь в список пар (символ, частота)
    items_list = []
    for char, count in char_count.items():
        items_list.append((char, count))
    
    # Сортировка пузырьком
    for i in range(len(items_list)):
        for j in range(0, len(items_list) - i - 1):
            if items_list[j][1] < items_list[j + 1][1]:
                # Меняем местами
                temp = items_list[j]
                items_list[j] = items_list[j + 1]
                items_list[j + 1] = temp
    
    print("\nСимвол | Частота")
    
    # Запись результатов в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Символ\tЧастота\n")
        
        for char, count in items_list:
            if char == '\n':
                display_char = '\\n'
            elif char == '\t':
                display_char = '\\t'
            elif char == ' ':
                display_char = 'пробел'
            elif char == '\r':
                display_char = '\\r'
            else:
                display_char = char
            
            print(f"{display_char:7} | {count}")
            f.write(f"{char}\t{count}\n")
    
    print(f"Всего различных символов: {len(items_list)}")

except FileNotFoundError:
    print(f"Файл {input_file} не найден")