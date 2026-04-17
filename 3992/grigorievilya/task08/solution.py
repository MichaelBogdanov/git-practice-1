import random
import string

# Ввод параметров
length = int(input("Длина пароля: "))
use_digits = input("Цифры? (y/n): ").lower() == 'y'
use_upper = input("Заглавные? (y/n): ").lower() == 'y'
use_lower = input("Строчные? (y/n): ").lower() == 'y'
use_special = input("Спецсимволы? (y/n): ").lower() == 'y'

# Собираем символы
chars = ''
if use_lower: chars += string.ascii_lowercase
if use_upper: chars += string.ascii_uppercase
if use_digits: chars += string.digits
if use_special: chars += string.punctuation

# Проверка
if not chars:
    print("Ошибка: выберите хоть что-то!")
    exit()

# Гарантия минимума (если длина позволяет)
if length >= len([use_lower, use_upper, use_digits, use_special]):
    password = []
    if use_lower: password.append(random.choice(string.ascii_lowercase))
    if use_upper: password.append(random.choice(string.ascii_uppercase))
    if use_digits: password.append(random.choice(string.digits))
    if use_special: password.append(random.choice(string.punctuation))
    
    for _ in range(length - len(password)):
        password.append(random.choice(chars))
    random.shuffle(password)
    password = ''.join(password)
else:
    password = ''.join(random.choice(chars) for _ in range(length))

print(f"\nПароль: {password}")