"""
Question:
Write a method that given a Linked List removes the duplicate values.

Input: [1, 3, 6, 3, 9, 1]
Output: [1, 3, 6, 9]
"""

from . import LinkedList
from unittest import TestCase


def remove_duplicate(ll):
    current = ll.head
    seen = set()

    while current is not None:
        next = current.next

        if current.value in seen:
            ll.remove(current)
        else:
            seen.add(current.value)

        current = next

    return ll


class Test(TestCase):
    def test_remove_duplicate(self):
        data = LinkedList((1, 3, 6, 3, 9, 1))
        expected = LinkedList((1, 3, 6, 9))

        self.assertEqual(expected, remove_duplicate(data))
