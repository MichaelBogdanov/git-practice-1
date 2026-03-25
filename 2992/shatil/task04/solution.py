"""
Задача 4 — Удаление дубликатов, сохраняя порядок

Считывает слова или числа из файла (через пробел) и выводит их
без повторений, сохраняя исходный порядок первого появления.
"""

import sys


def remove_duplicates(items: list) -> list:
    """Возвращает список без дубликатов, сохраняя исходный порядок."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def main():
    if len(sys.argv) < 2:
        print("Использование: python solution.py <файл>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        content = f.read()

    items = content.split()
    unique_items = remove_duplicates(items)

    print(" ".join(unique_items))


if __name__ == "__main__":
    main()
