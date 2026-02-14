def arabic_to_roman(num):
    if num < 1 or num > 3999:
        return "Ошибка: число должно быть от 1 до 3999"
    
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result = ""
    for i in range(len(values)):
        count = num // values[i]
        if count:
            result += symbols[i] * count
            num -= values[i] * count
    
    return result


def roman_to_arabic(roman):
    roman = roman.upper()
    
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    for char in roman:
        if char not in values:
            return "Ошибка: недопустимый символ"
    
    result = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = values[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    
    if result < 1 or result > 3999:
        return "Ошибка: число вне диапазона"
    
    if arabic_to_roman(result) != roman:
        return "Ошибка: некорректная римская запись"
    
    return result


user_input = input("Введите число (арабское или римское): ")

if user_input.isdigit():
    num = int(user_input)
    print(arabic_to_roman(num))
else:
    print(roman_to_arabic(user_input))
