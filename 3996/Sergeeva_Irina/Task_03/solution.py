# Чтение файла
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Убираем пробелы по краям и разбиваем на слова
words = text.strip().split()

# Переворачиваем порядок слов
answer = []
for i in range(len(words)-1, -1, -1):
    answer += [words[i]]

# Запись результата
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(answer))
