"""
Question:
Given a binary tree, write a function to get the maximum width of the given tree.
Width of a tree is maximum of widths of all levels.

For example:
    __1__
   /     \
  2       3
 / \       \
4   5       8
           / \
          6   7

For the above tree,
width of level 1 is 1.
width of level 2 is 2.
width of level 3 is 3.
width of level 4 is 2.

So the maximum width of the tree is 3.
"""

from binarytree import Node
from collections import deque
from unittest import TestCase


def find_max_width(root):
    q = deque(iterable=(root,))
    max_width = 0

    while len(q):
        count = len(q)

        if max_width < count:
            max_width = count

        while count:
            node = q.pop()
            count -= 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return max_width


class Test(TestCase):
    def test_find_max_width(self):
        root = Node(1)

        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)

        root.right.right = Node(8)

        root.right.right.left = Node(6)
        root.right.right.right = Node(7)

        self.assertEqual(3, find_max_width(root))
