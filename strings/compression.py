"""
Question:
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabccccaaa would become a2b1c4a3.
If the compressed string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a-z)
"""

from unittest import TestCase


def compress_string(s):
    if not s:
        return s

    compressed = []

    previous_char = s[0]
    counter = 0

    for c in s:
        if c == previous_char:
            counter += 1
        else:
            compressed.append(previous_char)
            compressed.append(str(counter))
            previous_char = c
            counter = 1

    compressed.append(previous_char)
    compressed.append(str(counter))

    if len(compressed) > len(s):
        return s

    return ''.join(compressed)


class Test(TestCase):
    def test_compression(self):
        self.assertEqual('a2b1c4a3', compress_string('aabccccaaa'))
        self.assertEqual('a', compress_string('a'))
        self.assertEqual('a4', compress_string('aaaa'))
        self.assertEqual('A2a2C3', compress_string('AAaaCCC'))
        self.assertEqual('abcd', compress_string('abcd'))
