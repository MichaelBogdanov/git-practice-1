def rle_encode(text):
    result = ""
    count = 0
    for i in range(len(text)):
        if i != len(text) - 1 and text[i] == text[i + 1]: # проверка на последний символ и равенство соседствующих
            count+=1
        else:
            result += f"{text[i]}{count+1}" # добавление символы к итоговой строке
            count = 0
    return result

def rle_decode(text):
    result = ""
    i = 0
    while i < len(text):
        char = text[i] # взятие символа
        i += 1 # взятие первой цифры количества
        num_start = i
        while i < len(text) and text[i].isdigit():
            i += 1
        count = int(text[num_start:i]) # количество символа
        result += char * count 
    return result


# print(rle_encode("AAABBCAACCCD"))
# print(rle_decode("A2B1C3A1C10D1"))