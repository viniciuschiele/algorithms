"""
Explanation:
Permutation is all possible arrangements of a set of things, where the order is important.
Palindrome is a word or phrase that is the same forwards and backwards.

A string to be a permutation of palindrome, each char must have an even count
and at most one char can have an odd count.

Question:
Given a string, write a function to check if it is a permutation of a palindrome.
"""

from unittest import TestCase


def is_permutation_of_palindrome(s):
    counter = [0] * 256
    count_odd = 0

    for c in s:
        char_code = ord(c)
        counter[char_code] += 1

        if counter[char_code] % 2 == 1:
            count_odd += 1
        else:
            count_odd -= 1

    return count_odd <= 1


class Test(TestCase):
    def test_valid_permutation_of_palindrome(self):
        self.assertTrue(is_permutation_of_palindrome('pali pali'))
        self.assertTrue(is_permutation_of_palindrome('abc111cba'))

    def test_non_permutation_of_palindrome(self):
        self.assertFalse(is_permutation_of_palindrome('pali'))
        self.assertFalse(is_permutation_of_palindrome('abc1112cba'))
