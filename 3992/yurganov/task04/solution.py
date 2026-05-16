# удаление дубликатов с сохранением порядка
import sys


def remove_duplicates(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        print("Файл не найден")
        return

    items = data.split()
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    print(" ".join(result))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python solution.py <файл>")
    else:
        remove_duplicates(sys.argv[1])
