import random
import string

n = int(input("Длина пароля: "))

use_digits = input("Цифры? (y/n): ").lower() == "y"
use_lower  = input("Строчные? (y/n): ").lower() == "y"
use_upper  = input("Прописные? (y/n): ").lower() == "y"
use_spec   = input("Спецсимволы? (y/n): ").lower() == "y"

digits = string.digits
lower  = string.ascii_lowercase
upper  = string.ascii_uppercase
spec   = "!@#$%^&*()-_=+[]{};:,.?/\\|`~"

sets = []
if use_digits: sets.append(digits)
if use_lower:  sets.append(lower)
if use_upper:  sets.append(upper)
if use_spec:   sets.append(spec)

if not sets:
    print("Ошибка: нужно выбрать хотя бы один набор символов")
    quit()

chars = "".join(sets)

password = []

if n >= len(sets):
    for s in sets:
        password.append(random.choice(s))

while len(password) < n:
    password.append(random.choice(chars))

random.shuffle(password)

print("Пароль:", "".join(password))
