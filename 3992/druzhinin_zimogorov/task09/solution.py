def rle_compress(s):
    if not s:
        return ""
    
    result = []
    count = 1
    prev = s[0]
    
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            result.append(prev + str(count))
            prev = c
            count = 1
    

    result.append(prev + str(count))
    
    return ''.join(result)

input_string = "AAABBBCCDAA"
compressed = rle_compress(input_string)
print(f"Исходная строка: {input_string}")
print(f"Сжатая строка: {compressed}")