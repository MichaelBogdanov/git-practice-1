import sys
import random
import string

length = int(sys.argv[1])
digits = '--no-digits' not in sys.argv
lower = '--no-lower' not in sys.argv
upper = '--no-upper' not in sys.argv
special = '--no-special' not in sys.argv

if not (digits or lower or upper or special):
    print("Ошибка, не выбраны опции")
    sys.exit(1)

sets = []
required = []

if digits:
    sets.append(string.digits)
    required.append(random.choice(string.digits))

if lower:
    sets.append(string.ascii_lowercase)
    required.append(random.choice(string.ascii_lowercase))

if upper:
    sets.append(string.ascii_uppercase)
    required.append(random.choice(string.ascii_uppercase))

if special:
    sets.append("!@#$%^&*")
    required.append(random.choice("!@#$%^&*"))

all_chars = ''.join(sets)
password = ''.join(required)

remaining = length - len(required)
for _ in range(remaining):
    password += random.choice(all_chars)

password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(password)
