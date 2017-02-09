"""
Question:
Given a sorted array which is rotated n number of times, find out how many times the array is rotated.
Time complexity should be less than O(n).

Input: {5, 6, 1, 2, 3, 4}
Output: 2

Input: {1, 2, 3, 4}
Output: 0

Input: {2, 1}
Output: 1
"""

from unittest import TestCase


def find_num_rotation(arr):
    low = 0
    high = len(arr) - 1

    while arr[low] > arr[high]:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return low


class Test(TestCase):
    def test_find_count_rotated(self):
        arr = [5, 6, 1, 2, 3, 4]
        self.assertEqual(2, find_num_rotation(arr))

        arr = [1, 2, 3, 4]
        self.assertEqual(0, find_num_rotation(arr))

        arr = [4, 3, 2, 1]
        self.assertEqual(3, find_num_rotation(arr))

        arr = [2, 1]
        self.assertEqual(1, find_num_rotation(arr))
