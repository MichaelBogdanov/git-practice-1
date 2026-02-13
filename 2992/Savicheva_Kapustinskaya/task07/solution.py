def count_chars(text, ignore_case=True):
    if ignore_case:
        text = text.lower()

    freq = {}
    for char in text:
        if char != '\n' and char != '\r':  # игнор переноса строк
            freq[char] = freq.get(char, 0) + 1

    # сортировка по убыванию частоты
    sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_freq

if __name__ == "__main__":
    choice = input("Игнорировать регистр? (y/n): ").lower()
    ignore = True if choice == 'y' else False

    print("Введите текст (для завершения введите пустую строку):")
    lines = []
    while True:
        line = input()
        if not line: break
        lines.append(line)

    content = " ".join(lines)
    result = count_chars(content, ignore)

    print("\nРезультат (Символ: Количество):")
    for char, count in result:
        print(f"'{char}': {count}")