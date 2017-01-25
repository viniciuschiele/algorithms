"""
Explanation:
Permutation is all possible arrangements of a set of things, where the order is important.

Question:
Given two strings, write a method to decide if one is a permutation of the other.
"""

from unittest import TestCase


def is_permutation(s1, s2):
    if not s1 or not s2:
        return False

    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


class Test(TestCase):
    def test_valid_permutation(self):
        self.assertTrue(is_permutation('abc', 'cab'))
        self.assertTrue(is_permutation('159', '915'))

    def test_invalid_permutation(self):
        self.assertFalse(is_permutation('abc', 'def'))
        self.assertFalse(is_permutation('123', '124'))
