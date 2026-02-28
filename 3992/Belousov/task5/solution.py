def function2():
    data_list = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    word = input("Введите число: ")
    converted_word = ""
    for letter, i in data_list.items():
        while word >= i:
            converted_word+=letter
            word-=i
    return converted_word


print(function2())