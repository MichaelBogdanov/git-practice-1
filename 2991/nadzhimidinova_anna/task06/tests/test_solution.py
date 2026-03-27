import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from solution import merge_sort, parse_input


class TestMergeSort(unittest.TestCase):

    def test_sort_unsorted_list(self):
        self.assertEqual(merge_sort([5, 2, 9, 1, 3]), [1, 2, 3, 5, 9])

    def test_sort_already_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_sort_with_duplicates(self):
        self.assertEqual(merge_sort([4, 2, 4, 1, 2]), [1, 2, 2, 4, 4])

    def test_sort_negative_numbers(self):
        self.assertEqual(merge_sort([-3, 7, 0, -1]), [-3, -1, 0, 7])

    def test_parse_input(self):
        self.assertEqual(parse_input("10 3 8 1"), [10, 3, 8, 1])


if __name__ == "__main__":
    unittest.main()