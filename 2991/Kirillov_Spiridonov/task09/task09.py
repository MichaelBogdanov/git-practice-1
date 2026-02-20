def encode(text):
    result = ""
    count = 1
    
    # проходим по строке начиная со второго символа
    for i in range(1, len(text)):
        # если символ такой же, как предыдущий — увеличивается счётчик
        if text[i] == text[i - 1]:
            count += 1
        # если символ изменился — записывается предыдущий и его количество
        else:
            result += text[i - 1] + str(count)
            count = 1

    # добавление последнего символа и его количества
    result += text[-1] + str(count)
    return result


def decode(text):
    result = ""
    i = 0        


    while i < len(text):
        char = text[i]
        i += 1
        count = ""   
        
        # пока идут цифры — добавляют их к числу
        while i < len(text) and text[i].isdigit():
            count += text[i]
            i += 1

        # добавляется символ нужное количество раз
        result += char * int(count)

    return result


s = input("Введите строку: ")

encoded = encode(s)
decoded = decode(encoded)

print("Сжатие:     ", encoded)
print("Восстановление:", decoded)