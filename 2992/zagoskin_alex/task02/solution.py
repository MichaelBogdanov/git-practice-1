def analyze_text(text: str):
    lines = text.splitlines()
    line_count = len(lines)

    words = text.split()
    word_count = len(words)

    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return line_count, word_count, longest_word


if __name__ == "__main__":
    import sys

    print("Введите текст (Ctrl+Z + Enter для окончания):")
    text = sys.stdin.read()

    lines, words, longest = analyze_text(text)

    print("Количество строк:", lines)
    print("Количество слов:", words)
    print("Самое длинное слово:", longest)