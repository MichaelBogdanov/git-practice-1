text = "ВаняЖивотное я привет"
words = text.split()
words.reverse()
result = ' '.join(words)
print("Исходный текст:", text)
print("Результат:     ", result)