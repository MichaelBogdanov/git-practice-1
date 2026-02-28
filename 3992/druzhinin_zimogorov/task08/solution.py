import random
import string

print("Генерация паролей\n")

length_password = int(input("Введите длину пароля: "))

digits_flag = int(input("Включать цифры? 1-Да | 0-Нет: "))
uppercase_flag = int(input("Включать прописные буквы? 1-Да | 0-Нет: "))
lowercase_flag = int(input("Включать строчные буквы? 1-Да | 0-Нет: "))
special_flag = int(input("Включать спецсимволы? 1-Да | 0-Нет: "))

charsets = []
if digits_flag:
    charsets.append(list(string.digits))
if uppercase_flag:
    charsets.append(list(string.ascii_uppercase))
if lowercase_flag:
    charsets.append(list(string.ascii_lowercase))
if special_flag:
    charsets.append(list(string.punctuation))

if not charsets:
    print("Ошибка: не выбран ни один набор символов.")
    exit()

password_chars = []

for i in charsets:
    password_chars.append(random.choice(i))

all_chars = []
for i in charsets:
    all_chars.extend(i)


for i in range(length_password - len(charsets)):
    password_chars.append(random.choice(all_chars))

password = ''.join(password_chars)

print(f"\nСгенерированный пароль: {password}")