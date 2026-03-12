import sys

def reverse_words_in_file(input_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # split() без аргументов разбивает строку по ЛЮБОМУ количеству 
        # пробельных символов и сразу удаляет лишние пробелы по краям.
        words = content.split()
        
        # Переворачиваем список слов
        reversed_words = words[::-1]
        
        # Собираем строку обратно, вставляя ровно один пробел между словами
        result = " ".join(reversed_words)
        
        return result

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_path}' не найден.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python reverse_solution.py <имя_файла.txt>")
        sys.exit(1)

    filename = sys.argv[1]
    output_text = reverse_words_in_file(filename)
    
    print("--- Результат переворота ---")
    print(output_text)