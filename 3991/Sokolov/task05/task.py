import re

class RomanConverter:
    ROMAN_REGEX = re.compile(
        r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    )
    
    INT_TO_ROMAN_MAP = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    ROMAN_TO_INT_MAP = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    @classmethod
    def to_roman(cls, number: int) -> str:
        if not isinstance(number, int) or not (1 <= number <= 3999):
            raise ValueError("Число должно быть целым от 1 до 3999")
        
        result = []
        for value, numeral in cls.INT_TO_ROMAN_MAP:
            while number >= value:
                result.append(numeral)
                number -= value
        return "".join(result)

    @classmethod
    def to_arabic(cls, roman: str) -> int:
        if not isinstance(roman, str) or not roman:
            raise ValueError("Строка не должна быть пустой")
        
        roman = roman.upper()
        if not cls.ROMAN_REGEX.match(roman):
            raise ValueError("Неверный формат римского числа")
        
        total = 0
        prev_value = 0
        for char in reversed(roman):
            current_value = cls.ROMAN_TO_INT_MAP[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
            
        return total
