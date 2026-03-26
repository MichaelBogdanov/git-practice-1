import argparse
import re
import sys

ROMAN_PATTERN = re.compile(
    r"^M{0,3}(CM|CD|D?C{0,3})"
    r"(XC|XL|L?X{0,3})"
    r"(IX|IV|V?I{0,3})$"
)

ROMAN_VALUES = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]


def arabic_to_roman(number: int) -> str:
    if not (1 <= number <= 3999):
        raise ValueError("Число должно быть в диапазоне от 1 до 3999.")

    result = []
    remaining = number

    for symbol, value in ROMAN_VALUES:
        while remaining >= value:
            result.append(symbol)
            remaining -= value

    return "".join(result)


def roman_to_arabic(roman: str) -> int:
    if not roman or not ROMAN_PATTERN.fullmatch(roman):
        raise ValueError("Некорректная римская запись.")

    index = 0
    result = 0

    for symbol, value in ROMAN_VALUES:
        while roman[index:index + len(symbol)] == symbol:
            result += value
            index += len(symbol)
            if index >= len(roman):
                return result

    return result


def detect_and_convert(value: str) -> str:
    value = value.strip().upper()

    if not value:
        raise ValueError("Пустой ввод.")

    if value.isdigit():
        return arabic_to_roman(int(value))

    return str(roman_to_arabic(value))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Конвертер римских и арабских чисел."
    )
    parser.add_argument(
        "value",
        help="Арабское число 1..3999 или римская запись."
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        print(detect_and_convert(args.value))
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
