"""
Задача 8: Генерато пароля
"""

import random
import string

print("Генератор пароля запущен!")

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    result = generate_password()
    print(f"Ваш пароль: {result}")