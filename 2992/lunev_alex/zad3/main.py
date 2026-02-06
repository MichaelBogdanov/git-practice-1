input_file = 'input.txt'
output_file = 'output.txt'

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Удаление лишних пробелов и разделение на слова
    text = text.strip()
    words = text.split()
    
    # Переворот
    reversed_words = []
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    
    result = ' '.join(reversed_words)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print("Результат:", result[:50] + ("..." if len(result) > 50 else ""))
    print("Результат сохранён в файл", output_file)

except FileNotFoundError:
    print(f"Файл {input_file} не найден")