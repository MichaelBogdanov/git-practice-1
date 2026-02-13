def rle_encode(text: str) -> str:
    """Кодирование RLE строки"""
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
    
    result.append(current_char + str(count))
    return "".join(result)

def rle_decode(encoded_text: str) -> str:
    """Декодирование RLE строки"""
    if not encoded_text:
        return ""
    result = []
    i = 0
    while i < len(encoded_text):
        char = encoded_text[i]
        i += 1

        count_char = ""
        while i < len(encoded_text) and encoded_text[i].isdigit():
            count_char += encoded_text[i]
            i += 1
        
        count = int(count_char)
        result.append(char * count)
    
    return "".join(result)
    
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 4:
        print("Использование:")
        print("python solution.py encode input.txt encoded.txt")
        print("python solution.py decode encoded.txt decoded.txt")
        sys.exit(1)
    
    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read().strip()
        
        if command == "encode":
            result = rle_encode(data)
        elif command == "decode":
            result = rle_decode(data)
        else:
            print(f"Ошибка: Неизвестная команда: {command}")
            sys.exit(1)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        
        print(f"Успех! Результат сохранён в {output_file}")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
