"""
Question:
BTree is given, return the longest path.

For example:
    __1__
   /     \
  2       3
 / \     / \
4   5   1   2
       /
      9

Output should be [1, 3, 1, 9].
"""

from binarytree import Node
from unittest import TestCase


def find_longest_path(root):
    levels = []
    _find_longest_path(root, levels, 0)
    return levels


def _find_longest_path(node, levels, index):
    found = False

    if index == len(levels):
        levels.append(node.value)
        found = True

    if node.left:
        found = _find_longest_path(node.left, levels, index + 1)

    if node.right:
        found = _find_longest_path(node.right, levels, index + 1) or found

    if found:
        levels[index] = node.value

    return found


class Test(TestCase):
    def test_find_longest_path(self):
        root = Node(1)

        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)

        root.right.left = Node(1)
        root.right.right = Node(2)

        root.right.left.left = Node(9)

        self.assertEqual([1, 3, 1, 9], find_longest_path(root))
