import re
import sys

def analyze_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = len(content.splitlines())
    words = re.findall(r'\b\w+\b', content)
    longest = max(words, key=len) if words else ''
    return lines, len(words), longest, len(longest)

if name == "main":
    lines, words, longest, length = analyze_text(sys.argv[1])
    print(f"Строк: {lines}")
    print(f"Слов: {words}")
    print(f"Самое длинное слово: '{longest}' (длина: {length})")