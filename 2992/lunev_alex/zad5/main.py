rim_to_arab = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

arab_to_rim = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

examples = [1987, 4, 'MCMLXXXVII', 'IV', 'XIX', 3999, 'MMMM']

for example in examples:
    print(f"\nНачали: {example}")
    
    # Преобразование из римского в арабсккое
    if isinstance(example, str):
        roman = example.upper()
        is_valid = True
        
        # Проверка допустимых символов
        valid_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
        for char in roman:
            if char not in valid_chars:
                is_valid = False
                print(f"Ошибка: недопустимый символ '{char}'")
                break
        
        if is_valid:
            try:
                result_num = 0
                prev_value = 0
                
                for char in reversed(roman):
                    value = rim_to_arab[char]
                    
                    if value < prev_value:
                        result_num -= value
                    else:
                        result_num += value
                    
                    prev_value = value

                print(f"Результат: {result_num}")
                    
            except Exception as e:
                print(f"Ошибка: {e}")

    # Преобразование из арабского в римское
    elif isinstance(example, int):
        number = example
        
        if number < 1 or number > 3999:
            print(f"Ошибка: число {number} вне диапазона 1-3999")
        else:
            result_roman = ""
            
            for value, numeral in arab_to_rim:
                while number >= value:
                    result_roman += numeral
                    number -= value
            
            print(f"Результат: {result_roman}")
    
    else:
        print("Неподдерживаемый тип данных")