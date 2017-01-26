"""
Question:
Write a method to replace all spaces in a string with "%20", you may assume that the string has sufficient space
at the end to hold the additional characters, and that you are given the true length of the string.
"""


from unittest import TestCase


def replace_spaces(chars, size):
    p = -1

    for i in range(size - 1, -1, -1):
        if chars[i] == ' ':
            chars[p] = '0'
            p -= 1
            chars[p] = '2'
            p -= 1
            chars[p] = '%'
            p -= 1
        else:
            chars[p] = chars[i]
            p -= 1

    return chars


class Test(TestCase):
    def test_replace(self):
        self.assertEqual(replace_spaces(list('abc def ghi    '), 11), list('abc%20def%20ghi'))
        self.assertEqual(replace_spaces(list('abc'), 3), list('abc'))
