"""Тесты для задачи 7 — Подсчёт частоты символов."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from solution import count_chars


def test_basic():
    result = dict(count_chars("aab"))
    assert result["a"] == 2
    assert result["b"] == 1


def test_sorted_by_frequency():
    result = count_chars("aaabbc")
    assert result[0] == ("a", 3)
    assert result[1] == ("b", 2)
    assert result[2] == ("c", 1)


def test_ignore_case():
    result = dict(count_chars("AaBb", ignore_case=True))
    assert result["a"] == 2
    assert result["b"] == 2


def test_case_sensitive():
    result = dict(count_chars("AaBb", ignore_case=False))
    assert result["A"] == 1
    assert result["a"] == 1
    assert result["B"] == 1
    assert result["b"] == 1


def test_empty():
    assert count_chars("") == []


def test_single_char():
    assert count_chars("x") == [("x", 1)]


if __name__ == "__main__":
    tests = [test_basic, test_sorted_by_frequency, test_ignore_case,
             test_case_sensitive, test_empty, test_single_char]
    passed = 0
    for t in tests:
        try:
            t()
            print(f"PASS: {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {t.__name__} — {e}")
    print(f"\n{passed}/{len(tests)} тестов прошло")
