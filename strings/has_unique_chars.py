"""
Question: Implement an algorithm to determine if a string has all unique characters.
"""


from unittest import TestCase


def has_unique_chars(s):
    if not s:
        return False

    # instantiate a list
    counter = [False] * 256

    for c in s:
        char_code = ord(c)  # get the ascii code

        if counter[char_code]:
            return False

        counter[char_code] = True

    return True


class Test(TestCase):
    def test_unique_chars(self):
        self.assertTrue(has_unique_chars('abcde'))

    def test_non_unique_chars(self):
        self.assertFalse(has_unique_chars('abcdc'))
