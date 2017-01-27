"""
Question:
Given an image represented by an NxN matrix, assuming the matrix has the same number of rows and columns,
write a method to rotate the image by 90 degrees.
"""

from unittest import TestCase


def rotate_90(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        for i in range(layer, n - layer - 1):
            top = matrix[layer][i]

            # top left = bottom left
            matrix[layer][i] = matrix[-1-i][layer]

            # bottom left = bottom right
            matrix[-1-i][layer] = matrix[-layer-1][-i-1]

            # bottom right = top right
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]

            # top right = top left
            matrix[i][-layer - 1] = top


class Test(TestCase):
    def test_rotate_matrix(self):
        matrix = [
            [1,  2,  3,  4, 5],
            [6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

        expected = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]

        rotate_90(matrix)

        self.assertEqual(expected, matrix)
