try:
    file = open("text.txt")
    mass = file.read().split()
    mass.reverse()
    print(*mass)

except FileNotFoundError:
    print("файл text.txt не найден")
