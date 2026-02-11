# Задача 07 — Подсчёт частоты символов

from collections import Counter

FILENAME = "test.txt"
IGNORE_CASE = True  # False — учитывать регистр, True — игнорировать

with open(FILENAME, encoding="utf-8") as f:
    text = f.read()

if IGNORE_CASE:
    text = text.lower()

freq = Counter(text)

for char, count in freq.most_common():
    if char != "\n":
        print(f"{repr(char)}: {count}")
