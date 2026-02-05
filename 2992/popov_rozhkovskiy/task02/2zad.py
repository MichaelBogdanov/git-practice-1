import re

path = input()

with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

l = len(c.splitlines())
w = len(re.findall(r'\b\w+\b', c))
lw = max(re.findall(r'\b\w+\b', c), key=len) if c.strip() else ""

print("Строк:", l, "Слов:", w, f"Самое длинное слово: '{lw}' Длина: {len(lw)}")

