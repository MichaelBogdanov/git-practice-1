"""Тесты для задачи 4 — Удаление дубликатов."""

import sys
import os
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from solution import remove_duplicates


def test_basic():
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]


def test_all_unique():
    assert remove_duplicates(["1", "2", "3"]) == ["1", "2", "3"]


def test_all_same():
    assert remove_duplicates(["x", "x", "x"]) == ["x"]


def test_empty():
    assert remove_duplicates([]) == []


def test_preserves_order():
    result = remove_duplicates(["banana", "apple", "banana", "orange", "apple"])
    assert result == ["banana", "apple", "orange"]


def test_numbers():
    assert remove_duplicates(["3", "1", "2", "1", "3"]) == ["3", "1", "2"]


if __name__ == "__main__":
    passed = 0
    tests = [test_basic, test_all_unique, test_all_same, test_empty,
             test_preserves_order, test_numbers]
    for t in tests:
        try:
            t()
            print(f"PASS: {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {t.__name__} — {e}")
    print(f"\n{passed}/{len(tests)} тестов прошло")
