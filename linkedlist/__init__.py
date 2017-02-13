class LinkedList(object):
    def __init__(self, values):
        self.head = None
        self.tail = None

        for value in values:
            self.add_back(value)

    def add_front(self, value):
        item = LinkedListItem(value)

        if self.head:
            self.head.prev = item
            item.next = self.head
            self.head = item
        else:
            self.head = self.tail = item

    def add_back(self, value):
        item = LinkedListItem(value)

        if self.tail:
            item.prev = self.tail
            self.tail.next = item
            self.tail = item
        else:
            self.head = self.tail = item

    def remove(self, item):
        if item.prev:
            item.prev.next = item.next
        elif item == self.head:
            self.head = item.next

        if item.next:
            item.next.prev = item.prev
        elif item == self.tail:
            self.tail = item.prev

        item.next = item.prev = None

    def __eq__(self, other):
        if other is None:
            return False

        current1 = self.head
        current2 = other.head

        while current1 or current2:
            if not current1 or not current2:
                return False

            if current1.value != current2.value:
                return False

            current1 = current1.next
            current2 = current2.next

        return True

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)


class LinkedListItem(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
