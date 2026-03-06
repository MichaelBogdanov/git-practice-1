def rle_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(("" if count == 1 else str(count)) + text[i - 1])
            count = 1
    result.append(("" if count == 1 else str(count)) + text[-1])
    return "".join(result)

def rle_decode(encoded: str) -> str:
    result = []
    count_str = ""
    for ch in encoded:
        if ch.isdigit():
            count_str += ch
        else:
            count = int(count_str) if count_str else 1
            result.append(ch * count)
            count_str = ""
    return "".join(result)

print("Введите 'exit' для выхода\n")

while True:
    print("1 - Закодировать\n2 - Декодировать")
    choice = input("Выбор: ").strip()

    if choice.lower() == "exit":
        break

    if choice == "1":
        text = input("Введите строку: ")
        encoded = rle_encode(text)
        print(f"Результат: {encoded}\n")

    elif choice == "2":
        text = input("Введите RLE-строку: ")
        try:
            decoded = rle_decode(text)
            print(f"Результат: {decoded}\n")
        except Exception:
            print("Ошибка: некорректная RLE-строка\n")

    else:
        print("Неверный выбор, попробуйте снова\n")
