import random

ListStringInput = input().split()
password = ''
length = int(10)
digits = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = uppercase.lower()
punct = '!@#%^&*~'

for _ in range(length):
    randomNumber = random.randint(1, 4)
    if randomNumber == 1 and ListStringInput[randomNumber - 1] == 'True':
        password += random.choice(digits)
    elif randomNumber == 2 and ListStringInput[randomNumber - 1] == 'True':
        password += random.choice(uppercase)
    elif randomNumber == 3 and ListStringInput[randomNumber - 1] == 'True':
        password += random.choice(lower)
    elif randomNumber == 4 and ListStringInput[randomNumber - 1] == 'True':
        password += random.choice(digits)

while len(password) < length:
    randomNumber = random.randint(1, 4)
    if randomNumber == 1:
        password += random.choice(digits)
    elif randomNumber == 2:
        password += random.choice(uppercase)
    elif randomNumber == 3:
        password += random.choice(lower)
    elif randomNumber == 4:
        password += random.choice(digits)
print(password)