"""
Question:
Write an algorithm such that if an element in a NxN matrix is 0, its entire row and column are set to 0.
"""

from unittest import TestCase


def fill_zero(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])

    columns = []
    rows = []

    for y in range(row_count):
        for x in range(column_count):
            if matrix[y][x] == 0:
                rows.append(y)
                columns.append(x)

    for y in rows:
        for x in range(column_count):
            matrix[y][x] = 0

    for x in columns:
        for y in range(row_count):
            matrix[y][x] = 0


class Test(TestCase):
    def test_fill_zero(self):
        matrix = [
            [1,  2,  3,  4,  0],
            [6,  0,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 0,  18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

        expected = [
            [0,  0, 0,  0,  0],
            [0,  0, 0,  0,  0],
            [11, 0, 13, 14, 0],
            [0,  0, 0,  0,  0],
            [21, 0, 23, 24, 0]
        ]

        fill_zero(matrix)

        self.assertEqual(expected, matrix)
