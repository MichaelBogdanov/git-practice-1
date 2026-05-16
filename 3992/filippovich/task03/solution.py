import sys

def reverse_word_order(text):
    "Убирает лишние пробелы и переворачивает порядок слов"
    words = text.strip().split()
    return ' '.join(reversed(words))

def main():
    if len(sys.argv) != 2:
        print("Использование: python solution.py <файл с текстом>")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            original_text = f.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        sys.exit(1)
    reversed_text = reverse_word_order(original_text)
    print("Перевёрнутый порядок слов:", reversed_text)

if __name__ == "__main__":
    main()