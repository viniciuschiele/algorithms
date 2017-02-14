"""
Question:
Implement a queue using two stacks.
"""

from unittest import TestCase


class Queue(object):
    def __init__(self, values=None):
        self._stack_enqueue = list()
        self._stack_dequeue = list()

        if values:
            for value in values:
                self.push(value)

    def push(self, value):
        self._stack_enqueue.append(value)

    def pop(self):
        if not len(self._stack_dequeue):
            while len(self._stack_enqueue):
                self._stack_dequeue.append(self._stack_enqueue.pop())

        if not len(self._stack_dequeue):
            raise IndexError('Queue empty')

        return self._stack_dequeue.pop()


class Test(TestCase):
    def test_queue(self):
        queue = Queue([1, 2, 3, 4, 5])

        self.assertEqual(1, queue.pop())
        self.assertEqual(2, queue.pop())

        queue.push(6)

        self.assertEqual(3, queue.pop())
        self.assertEqual(4, queue.pop())
        self.assertEqual(5, queue.pop())
        self.assertEqual(6, queue.pop())
