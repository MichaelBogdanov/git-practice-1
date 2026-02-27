def compress(text):
    if not text:
        return ""
    
    result = ""
    count = 1
    current = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current:
            count += 1
        else:
            result += current + str(count)
            current = text[i]
            count = 1
    
    result += current + str(count)
    return result

def decompress(text):
    if not text:
        return ""
    
    result = ""
    i = 0
    
    while i < len(text):
        char = text[i]
        i += 1
        
        num_str = ""
        while i < len(text) and text[i].isdigit():
            num_str += text[i]
            i += 1
        
        result += char * int(num_str)
    
    return result

# тест
text = input("введите строку для сжатия: ")
compressed = compress(text)
print(f"сжато: {compressed}")
print(f"восстановлено: {decompress(compressed)}")
