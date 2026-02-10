import random
import string

password = ""
symbols = ""

length = int(input("Введите длину пароля: "))

use_digits = input("Включить цифры? y/n: ") == "y"
use_lower = input("Включить строчные буквы? y/n: ") == "y"
use_upper = input("Включить прописные буквы? y/n: ") == "y"
use_special = input("Включить спецсимволы? y/n:") == "y"



if use_digits:
    digit = random.choice(string.digits)
    password += digit
    symbols += string.digits

if use_lower:
    lower = random.choice(string.ascii_lowercase)
    password += lower
    symbols += string.ascii_lowercase

if use_upper:
    upper = random.choice(string.ascii_uppercase)
    password += upper
    symbols += string.ascii_uppercase

if use_special:
    special = random.choice("!@#$%^&*()_+-=")
    password += special
    symbols += "!@#$%^&*()_+-="

if symbols == "":
    print("Не выбран ни один набор символов")
    exit()

if length < len(password):
    print("Длинна пароля слишком маленькая")
    exit()

while len(password) < length:
    password += random.choice(symbols)

password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)

print("Сгенерированный пароль:", password)
