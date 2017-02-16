"""
Question:
Given a root of a tree, and an integer k. Get all the nodes which are at k distance from root.

For example:
    __1__
   /     \
  2       3
 / \     / \
4   5   1   2
       /
      9

Distance: 2
Output: [4, 5, 1, 2].
"""

from binarytree import Node
from unittest import TestCase


def find_notes_at_distance(root, distance):
    result = []
    _find_notes_at_distance(root, distance, result)
    return result


def _find_notes_at_distance(node, distance, result):
    if node is None:
        return

    if distance == 0:
        result.append(node.value)
    else:
        _find_notes_at_distance(node.left, distance-1, result)
        _find_notes_at_distance(node.right, distance-1, result)


class Test(TestCase):
    def test_find_notes_at_distance(self):
        root = Node(1)

        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)

        root.right.left = Node(1)
        root.right.right = Node(2)

        root.right.left.left = Node(9)

        self.assertEqual([4, 5, 1, 2], find_notes_at_distance(root, 2))
