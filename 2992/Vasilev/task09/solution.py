import sys


def encode_rle(s: str) -> str:    #сжимает строку


    if not s:
        return ""

    encoded = []
    count = 1
    prev = s[0]

    #проход по строке начиная со второго символа
    for ch in s[1:]:
        if ch == prev:
            #сравнение с предыдущим символом
            count += 1
        else:
            encoded.append(prev + str(count))#если символ сменился
            prev = ch
            count = 1

    encoded.append(prev + str(count))

    return ''.join(encoded)


def decode_rle(encoded: str) -> str: #расшифровка строки
    decoded = []
    i = 0
    length = len(encoded)

    while i < length:

        ch = encoded[i]
        i += 1

        #сбор всего числа(если будет число а не цифра)
        num_str = ''
        while i < length and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1

        #проверка строки на ошибку
        if not num_str:
            raise ValueError("Неправильный ввод строки")

        count = int(num_str)


        decoded.append(ch * count)

    return ''.join(decoded)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    mode = sys.argv[1].lower()
    data = sys.argv[2]

    if mode == "encode":
        print(encode_rle(data))
    elif mode == "decode":
        try:
            print(decode_rle(data))
        except ValueError as e:
            print(f"ошибка: {e}")
            sys.exit(1)
    else:
        print("неверный режим")
        sys.exit(1)