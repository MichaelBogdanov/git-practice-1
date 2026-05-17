import random
import string
import sys

def generate_password(length, use_digits, use_upper, use_lower, use_spec):
    sets = []
    if use_digits: sets.append(string.digits)
    if use_upper:  sets.append(string.ascii_uppercase)
    if use_lower:  sets.append(string.ascii_lowercase)
    if use_spec:   sets.append(string.punctuation)

    if not sets:
        return "Ошибка: не выбраны наборы символов"

    password = []
    # Гарантируем минимум по одному символу из каждого набора
    for s in sets:
        password.append(random.choice(s))

    # Дозаполняем до нужной длины
    all_chars = "".join(sets)
    while len(password) < length:
        password.append(random.choice(all_chars))

    # Перемешиваем, чтобы первые символы не были предсказуемыми
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    print(generate_password(12, True, True, True, True))