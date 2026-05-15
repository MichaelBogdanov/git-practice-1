# Задача 9: Сжатие строки (Run-Length Encoding)

def compress(text):
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            if count > 1:
                result.append(str(count))
            current_char = char
            count = 1
    
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    
    return ''.join(result)

def decompress(compressed):
    if not compressed:
        return ""
    
    result = []
    i = 0
    
    while i < len(compressed):
        char = compressed[i]
        i += 1
        
        count_str = ""
        while i < len(compressed) and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        
        count = int(count_str) if count_str else 1
        result.append(char * count)
    
    return ''.join(result)

print("=" * 50)
print("Задача 9: RLE сжатие строки")
print("=" * 50)

# Тесты
test_strings = ["AAABBBCCDAA", "WWWWWWWWWWWWBWWWWWWWWWWWWBBB", "ABC", "A", ""]

print("Тестирование:")
print("-" * 30)
for original in test_strings:
    compressed = compress(original)
    decompressed = decompress(compressed)
    
    status = "✓" if decompressed == original else "✗"
    print(f"{status} '{original}'")
    print(f"   Сжато: '{compressed}'")
    print(f"   Распаковано: '{decompressed}'")
    print()

# Интерактивный режим
print("=" * 50)
print("Интерактивный режим")
print("Команды: compress <текст>, decompress <текст>, exit")

while True:
    cmd = input("> ").strip()
    if cmd.lower() == 'exit':
        break
    
    parts = cmd.split(maxsplit=1)
    if len(parts) != 2:
        print("Ошибка: введите 'compress <текст>' или 'decompress <текст>'")
        continue
    
    command, text = parts[0].lower(), parts[1]
    
    if command == 'compress':
        result = compress(text)
        print(f"'{text}' -> '{result}'")
    elif command == 'decompress':
        result = decompress(text)
        print(f"'{text}' -> '{result}'")
    else:
        print("Неизвестная команда")