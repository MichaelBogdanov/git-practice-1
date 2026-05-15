text = input("Введите строку: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Частота символов:")

for char, count in frequency.items():
    print(f"{char} : {count}")