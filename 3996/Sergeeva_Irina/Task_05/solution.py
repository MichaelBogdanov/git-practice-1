def to_roman(num):
    # Значения и соответствующие им римские символы
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    result = ''
    for i in range(len(numbers)):
        while num >= numbers[i]:
            result += letters[i]
            num -= numbers[i]
    return result


def from_roman(roman):
    # Соответствие символов и значений
    values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    result = 0
    prev = 0
    # Проход справа налево
    for i in range(len(roman)-1, -1, -1):
        curr = values[roman[i]]
        if curr < prev:
            result -= curr  # Вычитание
        else:
            result += curr  # Сложение
        prev = curr
    return result


print(to_roman(1987))
print(from_roman('IV'))
