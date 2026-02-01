import random, string

n = int(input("Длина: "))

sets = []
if input("Цифры? (y/n): ") == "y": sets.append(string.digits)
if input("Строчные? (y/n): ") == "y": sets.append(string.ascii_lowercase)
if input("Прописные? (y/n): ") == "y": sets.append(string.ascii_uppercase)
if input("Спецсимволы? (y/n): ") == "y": sets.append("!@#$%^&*")

if not sets: raise SystemExit("Не выбран ни один набор")

pwd = [random.choice(s) for s in sets[:n]]                 # минимум по одному (если n хватает)
pwd += [random.choice("".join(sets)) for _ in range(n-len(pwd))]
random.shuffle(pwd)

print("Пароль:", "".join(pwd))