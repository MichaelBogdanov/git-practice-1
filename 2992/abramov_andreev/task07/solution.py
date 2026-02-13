ignore_case = True

file = open('data.txt', 'r', encoding='utf-8')
text = file.read()
file.close()

if ignore_case:
    text = text.lower()

stats = {}
for i in text:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1

items = list(stats.items())
items.sort(key=lambda i: i[1], reverse=True)

for i in items:
    char = i[0]
    count = i[1]
    if char == "\n": char = "\\n"
    if char == " ": char = "' '"
    print(f"{char} | {count}")