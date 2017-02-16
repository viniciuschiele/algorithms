"""
Question:
Given a binary tree, return the values vertically.

For example:

    __1__
   /     \
  2       3
 / \     / \
4   5   6   7
         \   \
          8   9

Output: [[4], [2], [1, 5, 6], [3, 8], [7], [9]]
"""

from binarytree import Node
from collections import defaultdict
from unittest import TestCase


def find_vertical_order(root):
    vertical_values = defaultdict(list)

    _find_vertical_order(root, vertical_values, 0)

    return [vertical_values[distance] for distance in sorted(vertical_values.keys())]


def _find_vertical_order(node, vertical_values, distance):
    vertical_values[distance].append(node.value)

    if node.left:
        _find_vertical_order(node.left, vertical_values, distance-1)

    if node.right:
        _find_vertical_order(node.right, vertical_values, distance+1)


class Test(TestCase):
    def test_find_vertical_order(self):
        root = Node(1)

        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)

        root.right.left = Node(6)
        root.right.right = Node(7)

        root.right.left.right = Node(8)
        root.right.right.right = Node(9)

        expected = [[4], [2], [1, 5, 6], [3, 8], [7], [9]]

        self.assertEqual(expected, find_vertical_order(root))
