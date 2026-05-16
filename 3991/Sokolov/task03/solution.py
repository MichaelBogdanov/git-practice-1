import sys

def reverse_words():
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()
    reversed_text = ' '.join(words[::-1])
    return ''.join(reversed_text)

def main():
    print(reverse_words())

if __name__ == '__main__':
    main()