import argparse
import sys


def encode_rle(text: str) -> str:
    if text == "":
        return ""

    result = []
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}:{count};")
            current_char = char
            count = 1

    result.append(f"{current_char}:{count};")
    return "".join(result)


def decode_rle(text: str) -> str:
    if text == "":
        return ""

    result = []
    parts = text.split(";")

    for part in parts:
        if not part:
            continue

        if ":" not in part:
            raise ValueError("Некорректный формат RLE.")

        char, count_str = part.split(":", 1)

        if len(char) != 1:
            raise ValueError("Некорректный символ в RLE.")

        if not count_str.isdigit():
            raise ValueError("Некорректное количество.")

        count = int(count_str)
        if count <= 0:
            raise ValueError("Количество должно быть положительным.")

        result.append(char * count)

    return "".join(result)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="RLE-сжатие и декодирование.")
    parser.add_argument(
        "mode",
        choices=["encode", "decode"],
        help="Режим: encode или decode"
    )
    parser.add_argument("text", help="Строка для обработки")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.mode == "encode":
            print(encode_rle(args.text))
        else:
            print(decode_rle(args.text))
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
