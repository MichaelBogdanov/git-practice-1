def rle_encode(text):
    """Кодирование строки с помощью RLE"""
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
    return ''.join(result)

def rle_decode(encoded):
    """Декодирование RLE-строки"""
    if not encoded:
        return ""
    result = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        
        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        count = int(count_str)
        result.append(char * count)
    
    return ''.join(result)

def main():
    print("RLE СЖАТИЕ")
    print("1 - Кодировать")
    print("2 - Декодировать")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        text = input("Введите строку для кодирования: ")
        result = rle_encode(text)
        print(f"Результат: {result}")
    elif choice == "2":
        encoded = input("Введите строку для декодирования: ")
        result = rle_decode(encoded)
        print(f"Результат: {result}")
    else:
        print("Некорректный выбор")

if __name__ == "__main__":
    main()