import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from solution import merge_sort

assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([3, 1, 2]) == [1, 2, 3]
assert merge_sort([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]
assert merge_sort([10, -1, 0, 5]) == [-1, 0, 5, 10]
assert merge_sort([1, 1, 1]) == [1, 1, 1]  # одинаковые элементы

print("Все тесты пройдены!")
