import sys
from collections import Counter

file_name = sys.argv[1]
ignore_case = len(sys.argv) > 2 and sys.argv[2] == '--ignore-case'

with open(file_name, 'r', encoding='utf-8') as f:
    text = f.read()

if ignore_case:
    text = text.lower()

counts = Counter(text)
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for char, count in sorted_counts:
    print(f"'{char}': {count}")
