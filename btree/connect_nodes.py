"""
Question:
Write a function to connect all the adjacent nodes at the same level in a binary tree.

         Input Tree                         Output Tree
             1                                  1 -> NULL
          /    \
        2        3                           2 -> 3 -> NULL
       / \      /  \
      4   5    6    7                      4 -> 5 -> 6 -> 7 -> NULL
     / \             \
    8   9             10                8 > 9 > 10 -> NULL
"""

from collections import deque
from unittest import TestCase


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next_right = None


def connect_nodes(root):
    q = deque([root])

    while len(q):
        count = len(q)

        prev_node = None

        while count:
            count -= 1
            node = q.popleft()

            if prev_node:
                prev_node.next_right = node

            prev_node = node

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)


class Test(TestCase):
    def test_connect_nodes(self):
        root = Node(1)

        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)

        root.right.left = Node(6)
        root.right.right = Node(7)

        root.left.left.left = Node(8)
        root.left.left.right = Node(9)

        root.right.right.right = Node(10)

        connect_nodes(root)

        self.assertIsNone(root.next_right)

        self.assertEqual(3, root.left.next_right.value)

        self.assertEqual(5, root.left.left.next_right.value)
        self.assertEqual(6, root.left.left.next_right.next_right.value)
        self.assertEqual(7, root.left.left.next_right.next_right.next_right.value)

        self.assertEqual(9, root.left.left.left.next_right.value)
        self.assertEqual(10, root.left.left.left.next_right.next_right.value)
