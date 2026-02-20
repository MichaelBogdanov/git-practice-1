import sys

if len(sys.argv) < 2:
    filename = input("Введите имя файла: ")
    sys.argv.append(filename)

file = open(sys.argv[1], "r", encoding="utf-8")
text = file.read()
file.close()

# разбиваем на слова (лишние пробелы автоматически убираются)
words = text.split()

# переворачиваем список слов
words.reverse()

# соединяем обратно через один пробел
result = " ".join(words)

print(result)