import sys
import re

def solve():
    if len(sys.argv) < 2:
        print("Укажите путь к файлу")
        return

    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        row_count = len(lines)
        full_text = "".join(lines)
        
        # Заменяем пунктуацию на пробелы и делим на слова
        words = re.findall(r'\w+', full_text)
        word_count = len(words)
        
        if words:
            longest_word = max(words, key=len)
            longest_len = len(longest_word)
        else:
            longest_word = ""
            longest_len = 0

        print(f"Строк: {row_count}")
        print(f"Слов: {word_count}")
        print(f"Самое длинное слово: {longest_word} ({longest_len})")

    except FileNotFoundError:
        print("Файл не найден")

if __name__ == "__main__":
    solve()