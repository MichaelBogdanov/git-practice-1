IGNORE_CASE = True

text = input("Введите текст для анализа: ")
if IGNORE_CASE:
    text = text.lower()
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
ат
print("\nСимвол | Частота")
print("-" * 20)
for char, count in sorted_freq:
    if char == ' ':
        print(f"'пробел' | {count}")
    else:
        print(f"'{char}'    | {count}")