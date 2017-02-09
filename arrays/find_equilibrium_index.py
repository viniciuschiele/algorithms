"""
Explanation:
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal
to the sum of elements at higher indexes.

A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0

3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + A[4] + A[5]=0

Question:
Write a function that given an array, returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.
"""

from unittest import TestCase


def equilibrium(arr):
    left_sum = 0
    total_sum = sum(arr)

    for i in range(len(arr)):
        left_sum += arr[i]

        if left_sum == total_sum:
            return i

        total_sum -= arr[i]

    return -1


class Test(TestCase):
    def test_equilibrium(self):
        a = [-7, 1, 5, 2, -4, 3, 0]

        self.assertEqual(3, equilibrium(a))
