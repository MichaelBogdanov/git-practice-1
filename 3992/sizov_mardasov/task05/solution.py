# Задача 05 — Конвертер римских чисел
# Поддерживает числа от 1 до 3999
# Пример: 1987 -> MCMLXXXVII, IV -> 4

# Таблица: арабское -> римское (по убыванию)
ROMAN_TABLE = [
    (1000, "M"),
    (900,  "CM"),
    (500,  "D"),
    (400,  "CD"),
    (100,  "C"),
    (90,   "XC"),
    (50,   "L"),
    (40,   "XL"),
    (10,   "X"),
    (9,    "IX"),
    (5,    "V"),
    (4,    "IV"),
    (1,    "I"),
]


def arabic_to_roman(number):
    """Переводит арабское число (1-3999) в римское."""
    if not isinstance(number, int) or number < 1 or number > 3999:
        raise ValueError("Число должно быть целым от 1 до 3999")

    result = ""
    for value, numeral in ROMAN_TABLE:
        # Пока число >= текущего значения — добавляем символ и вычитаем
        while number >= value:
            result += numeral
            number -= value
    return result


def roman_to_arabic(roman):
    """Переводит римское число в арабское. Проверяет корректность строки."""
    roman = roman.upper().strip()

    # Словарь одиночных символов
    single = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # Проверка: только допустимые символы
    for char in roman:
        if char not in single:
            raise ValueError(f"Недопустимый символ: '{char}'")

    result = 0
    prev = 0  # значение предыдущего символа

    # Читаем строку справа налево
    for char in reversed(roman):
        current = single[char]
        # Если текущий символ меньше предыдущего — это вычитание (IV, IX и т.д.)
        if current < prev:
            result -= current
        else:
            result += current
        prev = current

    # Проверка: обратная конвертация должна дать ту же строку
    if arabic_to_roman(result) != roman:
        raise ValueError(f"Некорректная римская запись: '{roman}'")

    return result


def convert(value):
    """Определяет тип входных данных и конвертирует."""
    # Если передали число — переводим в римское
    if isinstance(value, int):
        return arabic_to_roman(value)
    # Если строка — пробуем как римское число
    if isinstance(value, str):
        return roman_to_arabic(value)
    raise TypeError("Ожидается int или str")


# --- Запуск ---
if __name__ == "__main__":
    print("Конвертер римских чисел (1–3999)")
    print("Введите число (например, 1987) или римское (например, IV)")
    print("Для выхода введите 'стоп'\n")

    while True:
        user_input = input("Введите значение: ").strip()
        if user_input.lower() in ("стоп", "stop", "exit", "quit"):
            break
        try:
            # Если введено число — парсим как int
            if user_input.isdigit():
                result = arabic_to_roman(int(user_input))
            else:
                result = roman_to_arabic(user_input)
            print(f"  Результат: {result}\n")
        except (ValueError, TypeError) as e:
            print(f"  Ошибка: {e}\n")
