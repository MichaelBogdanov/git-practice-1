import string
from random import choice


default_alphabets = [string.ascii_letters, string.digits, string.punctuation]


def password_generator(length: int, alpabets: list[str] = default_alphabets):
    password = ""
    for i in range(length):
        # Добавляем символ в пароль
        password += choice(alpabets[i % len(alpabets)])
    return password


print(password_generator(10))