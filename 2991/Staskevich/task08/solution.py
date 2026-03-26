import argparse
import secrets
import string
import sys


def generate_password(
    length: int,
    use_digits: bool,
    use_lower: bool,
    use_upper: bool,
    use_special: bool,
) -> str:
    if length <= 0:
        raise ValueError("Длина пароля должна быть положительной.")

    groups = []

    if use_digits:
        groups.append(string.digits)
    if use_lower:
        groups.append(string.ascii_lowercase)
    if use_upper:
        groups.append(string.ascii_uppercase)
    if use_special:
        groups.append("!@#$%^&*()-_=+[]{};:,.?/")

    if not groups:
        raise ValueError("Нужно включить хотя бы один набор символов.")

    if length < len(groups):
        raise ValueError(
            "Длина пароля меньше количества включённых наборов символов."
        )

    password_chars = [secrets.choice(group) for group in groups]
    all_chars = "".join(groups)

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    # Перемешивание без random.shuffle
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Генератор паролей.")
    parser.add_argument("length", type=int, help="Длина пароля.")
    parser.add_argument("--digits", action="store_true", help="Включить цифры.")
    parser.add_argument("--lower", action="store_true", help="Включить строчные буквы.")
    parser.add_argument("--upper", action="store_true", help="Включить заглавные буквы.")
    parser.add_argument("--special", action="store_true", help="Включить спецсимволы.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_digits=args.digits,
            use_lower=args.lower,
            use_upper=args.upper,
            use_special=args.special,
        )
        print(password)
    except ValueError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
