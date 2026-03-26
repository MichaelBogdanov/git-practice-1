"""
Задача 3: Переворот слов в тексте
"""

import re

def reverse_words(text):
    words = re.findall(r'\b\w+\b', text)
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            text = f.read()
        print(reverse_words(text))
    else:
        print("Введите текст для переворота слов:")
        text = input()
        print("Результат:")
        print(reverse_words(text))