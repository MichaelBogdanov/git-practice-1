import random
import string


def generate_password(length,
                      use_digits=True,
                      use_lower=True,
                      use_upper=True,
                      use_special=True):

    groups = []

    if use_digits:
        groups.append(string.digits)

    if use_lower:
        groups.append(string.ascii_lowercase)

    if use_upper:
        groups.append(string.ascii_uppercase)

    if use_special:
        groups.append("!@#$%^&*()")

    if not groups:
        return "Ошибка: нет выбранных символов"

    if length < len(groups):
        return "Ошибка: длина слишком маленькая"

    password = []

    for group in groups:
        password.append(random.choice(group))

    all_symbols = ''.join(groups)

    while len(password) < length:
        password.append(random.choice(all_symbols))

    random.shuffle(password)

    return ''.join(password)


length = int(input("Длина пароля: "))

password = generate_password(length)

print("Пароль:", password)