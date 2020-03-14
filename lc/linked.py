# Classes for programming practice with linked lists


import unittest


class Node:

    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    @property
    def val(self):
        return self.item

    @val.setter
    def val(self, value):
        self.item = value

    def __repr__(self):
        tail = repr(self.next)
        return f'Node({self.item!r}, {tail})'


class List:

    def __init__(self, items=()):
        head = None
        prev = None
        for item in items:
            curr = Node(item)
            if head is None:
                head = curr
            elif prev is None:
                prev = head
            if prev is not None:
                prev.next = curr
                prev = curr
        self._head = head

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    def __len__(self):
        length = 0
        curr = self._head
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def __iter__(self):
        curr = self._head
        while curr is not None:
            yield curr.item
            curr = curr.next

    def __repr__(self):
        contents = repr(list(self))
        return f'List({contents})'


class _ListTest(unittest.TestCase):

    def test_len(self):
        ll = List()
        self.assertEqual(0, len(ll))
        ll = List(range(10))
        self.assertEqual(10, len(ll))

    def test_iter(self):
        ll = List()
        self.assertEqual([], list(ll))
        ll = List(range(10))
        self.assertEqual(list(range(10)), list(ll))

    def test_repr(self):
        ll = List()
        self.assertEqual('List([])', repr(ll))
        ll = List(range(3))
        self.assertEqual('List([0, 1, 2])', repr(ll))
        ll = List('abc')
        self.assertEqual("List(['a', 'b', 'c'])", repr(ll))
