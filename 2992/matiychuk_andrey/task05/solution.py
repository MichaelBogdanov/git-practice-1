roman_to_arabic_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

arabic_to_roman = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def arabic_to_roman_convert(number):
    result = ""
    for value, symbol in arabic_to_roman:
        while number >= value:
            result += symbol
            number -= value
    return result


def roman_to_arabic_convert(roman):
    total = 0
    prev = 0

    for char in roman[::-1]:
        value = roman_to_arabic_map[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value

    return total


def is_valid_roman(roman):
    try:
        number = roman_to_arabic_convert(roman)
        if number < 1 or number > 3999:
            return False
        return arabic_to_roman_convert(number) == roman
    except:
        return False


def main():
    value = input("Введите число (арабское или римское): ").upper()

    if value.isdigit():
        number = int(value)
        if number < 1 or number > 3999:
            print("INVALID")
        else:
            print(arabic_to_roman_convert(number))
    else:
        if is_valid_roman(value):
            print(roman_to_arabic_convert(value))
        else:
            print("INVALID")


main()
