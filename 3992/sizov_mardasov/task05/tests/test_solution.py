import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from solution import arabic_to_roman, roman_to_arabic

# Тесты арабское -> римское
assert arabic_to_roman(1) == "I"
assert arabic_to_roman(4) == "IV"
assert arabic_to_roman(9) == "IX"
assert arabic_to_roman(1987) == "MCMLXXXVII"
assert arabic_to_roman(3999) == "MMMCMXCIX"
assert arabic_to_roman(58) == "LVIII"

# Тесты римское -> арабское
assert roman_to_arabic("IV") == 4
assert roman_to_arabic("IX") == 9
assert roman_to_arabic("MCMLXXXVII") == 1987
assert roman_to_arabic("LVIII") == 58

# Тест некорректного ввода
try:
    arabic_to_roman(0)
    assert False, "Должна быть ошибка"
except ValueError:
    pass

try:
    roman_to_arabic("IIII")  # некорректная запись
    assert False, "Должна быть ошибка"
except ValueError:
    pass

print("Все тесты пройдены!")
