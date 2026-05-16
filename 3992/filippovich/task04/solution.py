import sys

def remove_duplicates(items):
    "Удаляет повторяющиеся элементы, сохраняя исходный порядок"
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def main():
    if len(sys.argv) != 2:
        print("Использование: python solution.py <файл со словами/числами>")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read().strip().split()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        sys.exit(1)
    unique_items = remove_duplicates(data)
    print("Элементы без дубликатов:", ' '.join(unique_items))

if __name__ == "__main__":
    main()