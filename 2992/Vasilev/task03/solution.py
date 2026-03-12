import sys

def reverse_words(text: str) -> str:
    # переворачивает порядок слов в строке, удаляя лишние пробелы

    words = text.split()
    return ' '.join(reversed(words))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"файл  не найден.")
        sys.exit(1)
    result = reverse_words(content)
    print(result)