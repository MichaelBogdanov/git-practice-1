import sys
import os

def encode_rle(text):
    if not text:
        return ""
    result = []
    count = 1
    # Идем по строке, сравнивая текущий символ со следующим
    for i in range(len(text)):
        if i + 1 < len(text) and text[i] == text[i+1]:
            count += 1
        else:
            # Как только символ сменился, записываем старый и его количество
            result.append(f"{text[i]}{count}")
            count = 1
    return "".join(result)

def decode_rle(text):
    if not text:
        return ""
    result = []
    i = 0
    while i < len(text):
        char = text[i]
        # Предполагаем, что за символом всегда идет число (минимум 1 цифра)
        # Собираем число (на случай, если оно двузначное и более)
        i += 1
        num_str = ""
        while i < len(text) and text[i].isdigit():
            num_str += text[i]
            i += 1
        if num_str:
            result.append(char * int(num_str))
    return "".join(result)

def main():
    if len(sys.argv) < 2:
        print("Использование: python rle_solution.py <имя_файла.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    encoded = encode_rle(content)
    decoded = decode_rle(encoded)

    print(f"--- RLE Сжатие файла: {file_path} ---")
    print(f"Исходная строка: {content}")
    print(f"Сжатая строка:   {encoded}")
    print(f"Распакованная:   {decoded}")
    
    # Проверка на корректность
    if content == decoded:
        print("\n[Успех] Данные полностью восстановлены.")
    else:
        print("\n[Ошибка] Данные повреждены при распаковке.")

if __name__ == "__main__":
    main()