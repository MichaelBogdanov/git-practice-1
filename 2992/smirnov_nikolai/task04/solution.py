# Удаление дубликатов с сохранением порядка

filename = "test.txt"

with open(filename, encoding="utf-8") as f:
    items = f.read().split()

seen = set()
result = []

for item in items:
    if item not in seen:
        seen.add(item)
        result.append(item)

print(" ".join(result))
