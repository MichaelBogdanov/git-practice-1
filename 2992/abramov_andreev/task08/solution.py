import random
import string

length = 12
use_digits = True
use_upper = True
use_lower = True
use_spec = True

sets = []
if use_digits: sets.append(string.digits)
if use_upper:  sets.append(string.ascii_uppercase)
if use_lower:  sets.append(string.ascii_lowercase)
if use_spec:   sets.append(string.punctuation)

password = []

for i in sets:
    password.append(random.choice(i))

all_chars = "".join(sets)
remaining_length = length - len(password)

for i in range(remaining_length):
    password.append(random.choice(all_chars))

random.shuffle(password)
final_password = "".join(password)
print("Ваш пароль:", final_password)