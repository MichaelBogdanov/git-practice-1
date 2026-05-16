# программа для подсчета строк, слов и поиска самого длинного слова
import sys
import re


def count_stats(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Файл не найден")
        return

    line_count = len(lines)
    word_count = 0
    longest_word = ""
    max_len = 0

    for line in lines:
        words = re.findall(r"[a-zA-Zа-яА-Я0-9]+", line)
        word_count += len(words)
        for word in words:
            if len(word) > max_len:
                max_len = len(word)
                longest_word = word

    print(f"Строк: {line_count}")
    print(f"Слов: {word_count}")
    print(f"Самое длинное слово: {longest_word} ({max_len})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python solution.py <файл>")
    else:
        count_stats(sys.argv[1])
