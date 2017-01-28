"""
Question:
Given a list of integers, write a method to write all permutations of the list, do this in O(1) space.
"""

from unittest import TestCase


def find_permutations(arr):
    permutations = []

    for c in range(len(arr)):
        for i in range(len(arr)-1):
            permutations.append(list(arr))

            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp

    return permutations


class Test(TestCase):
    def test_find_permutations(self):
        data = [1, 2, 3]
        expected = [[1, 2, 3],
                    [2, 1, 3],
                    [2, 3, 1],
                    [3, 2, 1],
                    [3, 1, 2],
                    [1, 3, 2]]

        self.assertEqual(expected, find_permutations(data))
