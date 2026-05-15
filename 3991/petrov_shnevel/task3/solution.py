text = input("Введите текст: ")

words = text.split()

words.reverse()

result = " ".join(words)

print("Результат:")
print(result)