# 5) Римские числа (двунаправленный конвертер)
# Цель: преобразование между римскими и арабскими числами
# Требования:
# Поддержка значений от 1 до 3999
# Валидация римской строки (правила составления)

class RomanConverter:
    # таблица соответствия римских чисел арабским
    ROMAN_TO_ARABIC = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    
    # таблица для преобразования из арабских в римские
    ARABIC_TO_ROMAN = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    @staticmethod
    def is_valid_roman(roman_num):
        roman = roman_num.upper()
        
        # проверяем допустимые символы
        valid_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
        for char in roman:
            if char not in valid_chars:
                return False
        
        if not roman:
            return False
        
        try:
            result = RomanConverter._convert_to_arabic(roman)
            return 1 <= result <= 3999
        except:
            return False
    
    @staticmethod
    def _convert_to_arabic(roman):
        result = 0
        i = 0
        
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i+2] in RomanConverter.ROMAN_TO_ARABIC:
                result += RomanConverter.ROMAN_TO_ARABIC[roman[i:i+2]]
                i += 2
            elif roman[i] in RomanConverter.ROMAN_TO_ARABIC:
                result += RomanConverter.ROMAN_TO_ARABIC[roman[i]]
                i += 1
            else:
                raise ValueError("Некорректный символ")
        
        return result
    
    @staticmethod
    def roman_to_arabic(roman_num):
        if not roman_num:
            return None
            
        if not RomanConverter.is_valid_roman(roman_num):
            return None
        
        try:
            return RomanConverter._convert_to_arabic(roman_num.upper())
        except:
            return None
    
    @staticmethod
    def arabic_to_roman(arabic_num):
        try:
            number = int(arabic_num)
        except ValueError:
            return None
        
        # проверяем диапазон
        if number < 1 or number > 3999:
            return None
        
        result = []
        for value, symbol in RomanConverter.ARABIC_TO_ROMAN:
            while number >= value:
                result.append(symbol)
                number -= value
        
        return ''.join(result)


def main():
    print("КОНВЕРТЕР РИМСКИХ ЧИСЕЛ")
    print("=" * 40)
    print("1. Арабское → Римское")
    print("2. Римское → Арабское")
    print("3. Выход")
    
    while True:
        print("\n" + "=" * 40)
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == '1':
            # Арабское в Римское
            value = input("Введите арабское число (1-3999): ").strip()
            roman = RomanConverter.arabic_to_roman(value)
            
            if roman:
                print(f"{value} → {roman}")
            else:
                print("Ошибка: число должно быть от 1 до 3999")
        
        elif choice == '2':
            # Римское в Арабское
            value = input("Введите римское число: ").strip()
            arabic = RomanConverter.roman_to_arabic(value)
            
            if arabic:
                print(f"{value.upper()} → {arabic}")
            else:
                print("Ошибка: некорректное римское число")
        
        elif choice == '3':
            print("Выход из программы.")
            break
        
        else:
            print("Ошибка: выберите 1, 2 или 3")


if __name__ == "__main__":
    main()