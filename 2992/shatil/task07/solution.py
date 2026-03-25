"""
Задача 7 — Подсчёт частоты символов

Считывает файл и выводит частоту каждого символа,
отсортированную по убыванию.

Использование:
    python solution.py <файл> [--ignore-case]
"""

import sys
from collections import Counter


def count_chars(text: str, ignore_case: bool = False) -> list[tuple[str, int]]:
    """
    Подсчитывает частоту символов в тексте.

    Args:
        text: входной текст
        ignore_case: если True, приводит символы к нижнему регистру

    Returns:
        Список пар (символ, количество), отсортированный по убыванию частоты.
    """
    if ignore_case:
        text = text.lower()

    counts = Counter(text)
    # Сортируем по убыванию частоты, при равенстве — по символу
    return sorted(counts.items(), key=lambda x: (-x[1], x[0]))


def format_char(ch: str) -> str:
    """Возвращает читаемое представление символа."""
    if ch == " ":
        return "SPACE"
    if ch == "\n":
        return "NEWLINE"
    if ch == "\t":
        return "TAB"
    return repr(ch) if not ch.isprintable() else ch


def main():
    if len(sys.argv) < 2:
        print("Использование: python solution.py <файл> [--ignore-case]")
        sys.exit(1)

    filename = sys.argv[1]
    ignore_case = "--ignore-case" in sys.argv

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    results = count_chars(text, ignore_case)

    mode = "(без учёта регистра)" if ignore_case else "(с учётом регистра)"
    print(f"Частота символов {mode}:")
    print(f"{'Символ':<12} {'Частота':>8}")
    print("-" * 22)
    for ch, count in results:
        print(f"{format_char(ch):<12} {count:>8}")


if __name__ == "__main__":
    main()
