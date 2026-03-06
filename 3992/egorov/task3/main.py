import sys

def reverse_words(text):
    words = text.strip().split()
    return ' '.join(words[::-1])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Укажите имя файла")
        sys.exit(1)
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        content = f.read()
    result = reverse_words(content)
    print(result)