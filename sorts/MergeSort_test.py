import unittest
from MergeSort import mergesort
from MergeSort import merge


class TestMergeSort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(mergesort([]), [])

    def test_odd(self):
        self.assertEqual(mergesort([1, 4, 3]), [1, 3, 4])

    def test_regular(self):
        self.assertEqual(mergesort([5, 4, 7, 8, 1, 2, 6, 3]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_duplicates(self):
        self.assertEqual(mergesort([10, 7, 1, 3, 3, 8, 9, 10]), [1, 3, 3, 7, 8, 9, 10, 10])
