import random

numbers = "0123456789"
uppercase_latin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_latin = "abcdefghijklmnopqrstuvwxyz"
special_symbols = "!@#$%^&*()-_=+[]{};:,.?/"
all_symbols = numbers + uppercase_latin + lowercase_latin + special_symbols
result = ""

pwd_length = int(input("Введите длину пароля: "))

excluded_chars = input("Какие символы вы хотите исключить?: ")

all_left_symbols = all_symbols
for ex_char in excluded_chars:
    all_left_symbols = all_left_symbols.replace(ex_char, "")

try:
    print("Сгенерированный пароль: ", result.join(random.sample(all_left_symbols, pwd_length)))
except ValueError:
    print("Длина пароля больше количества доступных символов")




