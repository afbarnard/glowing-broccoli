# Generic tests for data structures

import builtins
import itertools as itools
import unittest


KEY_RANGE = range(10)
VALUE_RANGE = range(1000)

# Some random (key, value) pairs
map_data = (
    (0, 764),
    (3, 448),
    (8, 760),
    (7, 648),
    (4, 307),
    (9, 384),
    (7, 682),
    (5, 841),
    (1, 152),
    (3, 102),
    (5, 114),
    (0, 555),
    (7, 485),
    (8, 255),
    (0, 229),
    (3, 623),
    (0, 222),
    (2, 653),
    (1, 927),
    (1, 233),
)

class SetTest(unittest.TestCase):

    def _new(self, items=()):
        """Subclasses should override this to create their own set instances."""
        return set(items)

    def test_len_empty(self):
        _set = self._new()
        self.assertEqual(0, len(_set))

    def test_len(self):
        _set = self._new(KEY_RANGE)
        self.assertEqual(len(KEY_RANGE), len(_set))

    def test_contains_empty(self):
        _set = self._new()
        for key in KEY_RANGE:
            self.assertNotIn(key, _set)

    def test_contains(self):
        _set = self._new(KEY_RANGE)
        for key in KEY_RANGE:
            self.assertIn(key, _set)

    def test_add(self):
        _set = self._new()
        correct = set()
        universe = set(KEY_RANGE)
        # Add each key twice
        for key in itools.chain(KEY_RANGE, KEY_RANGE):
            correct.add(key)
            _set.add(key)
            # Check size
            self.assertEqual(len(correct), len(_set))
            # Check contents
            for item in correct:
                self.assertIn(item, _set)
            for item in universe - correct:
                self.assertNotIn(item, _set)

    def test_discard(self):
        _set = self._new()
        correct = set()
        universe = set(KEY_RANGE)
        # Load it up!
        for key in KEY_RANGE:
            correct.add(key)
            _set.add(key)
        # Delete them all!
        for key in itools.chain(KEY_RANGE, KEY_RANGE):
            correct.discard(key)
            _set.discard(key)
            # Check size
            self.assertEqual(len(correct), len(_set))
            # Check contents
            for item in correct:
                self.assertIn(item, _set)
            for item in universe - correct:
                self.assertNotIn(item, _set)
        self.assertEqual(0, len(_set))


class ListHeap(list):

    def add(self, item):
        self.append(item)

    def discard(self, item):
        if item in self:
            self.remove(item)

    def max(self):
        if not self:
            raise LookupError('Empty heap')
        return builtins.max(self)

    def pop(self):
        if not self:
            raise LookupError('Empty heap')
        m = max(self)
        self.remove(m)
        return m

    def update(self, old, new):
        if old not in self:
            return
        i = self.index(old)
        self[i] = new


class HeapTest(unittest.TestCase):

    def _new(self, items=()):
        return ListHeap(items)

    def test_len_empty(self):
        heap = self._new()
        self.assertEqual(0, len(heap))

    def test_len(self):
        heap = self._new(KEY_RANGE)
        self.assertEqual(len(KEY_RANGE), len(heap))

    def test_contains_empty(self):
        heap = self._new()
        for key in KEY_RANGE:
            self.assertNotIn(key, heap)

    def test_contains(self):
        heap = self._new(KEY_RANGE)
        for key in KEY_RANGE:
            self.assertIn(key, heap)

    def test_add(self):
        heap = self._new()
        correct = []
        universe = set(KEY_RANGE)
        for key in itools.chain(KEY_RANGE, KEY_RANGE):
            correct.append(key)
            heap.add(key)
            # Check size
            self.assertEqual(len(correct), len(heap))
            # Check contents
            for item in correct:
                self.assertIn(item, heap)
            for item in universe - set(correct):
                self.assertNotIn(item, heap)

    def test_discard(self):
        heap = self._new()
        correct = []
        universe = set(KEY_RANGE)
        # Load it up!
        for key in itools.chain(KEY_RANGE, KEY_RANGE):
            correct.append(key)
            heap.add(key)
        # Delete them all!
        for key in itools.chain(KEY_RANGE, KEY_RANGE, KEY_RANGE):
            if key in correct:
                correct.remove(key)
            heap.discard(key)
            # Check size
            self.assertEqual(len(correct), len(heap))
            # Check contents
            for item in correct:
                self.assertIn(item, heap)
            for item in universe - set(correct):
                self.assertNotIn(item, heap)
        self.assertEqual(0, len(heap))

    def test_max_empty(self):
        heap = self._new()
        self.assertRaises(LookupError, heap.max)

    def test_max(self):
        heap = self._new(KEY_RANGE)
        self.assertEqual(KEY_RANGE[-1], heap.max())

    def test_pop_empty(self):
        heap = self._new()
        self.assertRaises(LookupError, heap.pop)

    def test_pop(self):
        heap = self._new(KEY_RANGE)
        for item in reversed(KEY_RANGE):
            self.assertEqual(item, heap.pop())

    def test_extend(self):
        heap = self._new()
        heap.extend(KEY_RANGE)
        key_max = KEY_RANGE[-1]
        self.assertEqual(key_max, heap.max())
        for item in KEY_RANGE:
            self.assertIn(item, heap)
        hi_range = range(key_max + 1, key_max + 11)
        heap.extend(hi_range)
        self.assertEqual(hi_range[-1], heap.max())
        for item in range(KEY_RANGE[0], hi_range[-1] + 1):
            self.assertIn(item, heap)

    def test_update_empty(self):
        heap = self._new()
        heap.update(1, 2)
        self.assertNotIn(1, heap)
        self.assertNotIn(2, heap)
        self.assertEqual(0, len(heap))

    def _check_update(self, heap, old_val, new_val, old_max, new_max):
        self.assertIn(old_val, heap)
        self.assertNotIn(new_val, heap)
        self.assertEqual(old_max, heap.max())
        heap.update(old_val, new_val)
        self.assertNotIn(old_val, heap)
        self.assertIn(new_val, heap)
        self.assertEqual(new_max, heap.max())

    def test_update_decrease_max(self):
        heap = self._new(KEY_RANGE)
        max = KEY_RANGE[-1]
        self._check_update(heap, max, -max, max, max - 1)

    def test_update_increase_to_max(self):
        heap = self._new(KEY_RANGE)
        middle = (KEY_RANGE[0] + KEY_RANGE[-1]) // 2
        max = KEY_RANGE[-1]
        new_max = max + 1
        self._check_update(heap, middle, new_max, max, new_max)

    def test_update_decrease_to_min(self):
        heap = self._new(KEY_RANGE)
        middle = (KEY_RANGE[0] + KEY_RANGE[-1]) // 2
        max = KEY_RANGE[-1]
        self._check_update(heap, middle, -middle, max, max)
