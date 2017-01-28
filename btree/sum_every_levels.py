"""
Question:
BTree is given, calculate and return array with a sum of every level.

For example:
    __1__
   /     \
  2       3
 / \     / \
4   5   1   2

Output should be [1, 5, 12].
"""

from binarytree import Node
from unittest import TestCase


def sum_levels(root):
    levels = []
    sum_level(root, levels, 0)
    return levels


def sum_level(node, levels, index):
    if index == len(levels):
        levels.append(node.value)
    else:
        levels[index] += node.value

    if node.left:
        sum_level(node.left, levels, index + 1)

    if node.right:
        sum_level(node.right, levels, index + 1)


class Test(TestCase):
    def test_sum_levels(self):
        root = Node(1)

        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)

        root.right.left = Node(1)
        root.right.right = Node(2)

        self.assertEqual([1, 5, 12], sum_levels(root))
