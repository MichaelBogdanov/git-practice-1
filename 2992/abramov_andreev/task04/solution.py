file = open('data.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

words = content.split()
result = []

for i in words:
    if i not in result:
        result.append(i)

print("Результат:", " ".join(result))