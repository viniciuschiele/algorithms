"""
Question:
Given two binary trees, check if the second tree is subtree of the first one.

For example:

        Tree 1                Tree 2
          26                    10
        /   \                  /  \
      10     3                4    6
    /   \    \                \
  4      6    3                30
   \
    30

Output: True
"""

from binarytree import Node
from unittest import TestCase


def is_subtree(tree1, tree2):
    if tree1 is None or tree2 is None:
        return False

    if compare_trees(tree1, tree2):
        return True

    if is_subtree(tree1.left, tree2):
        return True

    if is_subtree(tree1.right, tree2):
        return True

    return False


def compare_trees(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True

    if tree1 is None or tree2 is None:
        return False

    if tree1.value != tree2.value:
        return False

    if not compare_trees(tree1.left, tree2.left):
        return False

    if not compare_trees(tree1.right, tree2.right):
        return False

    return True


class Test(TestCase):
    def test_is_subtree(self):
        tree1 = Node(26)
        tree1.left = Node(10)
        tree1.right = Node(3)
        tree1.left.left = Node(4)
        tree1.left.right = Node(6)
        tree1.left.left.right = Node(30)
        tree1.right.right = Node(3)

        tree2 = Node(10)
        tree2.left = Node(4)
        tree2.left.right = Node(30)
        tree2.right = Node(6)

        self.assertEqual(True, is_subtree(tree1, tree2))
