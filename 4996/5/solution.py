# Задача 5: Римские числа (двунаправленный конвертер)

ROMAN_VALUES = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

ARABIC_TO_ROMAN = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

def roman_to_arabic(roman):
    if not roman:
        raise ValueError("Пустая строка")
    
    roman = roman.upper()
    result = 0
    prev_value = 0
    
    for char in reversed(roman):
        if char not in ROMAN_VALUES:
            raise ValueError(f"Некорректный символ: {char}")
        
        curr_value = ROMAN_VALUES[char]
        
        if curr_value < prev_value:
            result -= curr_value
        else:
            result += curr_value
        
        prev_value = curr_value
    
    return result

def arabic_to_roman(number):
    if not 1 <= number <= 3999:
        raise ValueError(f"Число должно быть 1-3999, получено: {number}")
    
    result = []
    remaining = number
    
    for value, symbol in ARABIC_TO_ROMAN:
        while remaining >= value:
            result.append(symbol)
            remaining -= value
    
    return ''.join(result)

print("=" * 50)
print("Задача 5: Конвертер римских чисел")
print("=" * 50)

# Тесты
test_romans = ["I", "IV", "IX", "X", "XL", "XC", "CD", "CM", "MCMXCIV", "MMXXIII"]
print("\nРимские -> Арабские:")
for r in test_romans:
    a = roman_to_arabic(r)
    print(f"{r} = {a}")

test_numbers = [1, 4, 9, 10, 40, 90, 400, 900, 1994, 2023]
print("\nАрабские -> Римские:")
for n in test_numbers:
    r = arabic_to_roman(n)
    print(f"{n} = {r}")

# Интерактивный режим
print("\nИнтерактивный режим")
print("Команды: roman XIV, arabic 2024, exit")

while True:
    cmd = input("> ").strip()
    if cmd.lower() == 'exit':
        break
    
    parts = cmd.split()
    if len(parts) != 2:
        print("Ошибка: введите 'roman <число>' или 'arabic <число>'")
        continue
    
    command, value = parts[0].lower(), parts[1]
    
    try:
        if command == 'roman':
            result = roman_to_arabic(value)
            print(f"{value} = {result}")
        elif command == 'arabic':
            num = int(value)
            result = arabic_to_roman(num)
            print(f"{num} = {result}")
        else:
            print("Неизвестная команда")
    except Exception as e:
        print(f"Ошибка: {e}")