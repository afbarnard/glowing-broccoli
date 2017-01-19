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


class SortTest(unittest.TestCase):

    def _new(self):
        return sorted

    def test_empty(self):
        sort = self._new()
        self.assertEqual([], sort([]))

    def test_sort_1(self):
        sort = self._new()
        things = [6]
        answer = [6]
        result = sort(things)
        self.assertEqual(answer, result)

    def test_sort_2(self):
        sort = self._new()
        things = [5, 7]
        answer = [5, 7]
        result = sort(things)
        self.assertEqual(answer, result)
        sort = self._new()
        things = [8, 1]
        answer = [1, 8]
        result = sort(things)
        self.assertEqual(answer, result)

    def test_sort_11(self):
        sort = self._new()
        things = [2, 1, 6, 8, 2, 7, 3, 6, 1, 3, 0]
        answer = [0, 1, 1, 2, 2, 3, 3, 6, 6, 7, 8]
        result = sort(things)
        self.assertEqual(answer, result)

    def test_increasing(self):
        sort = self._new()
        things = [1, 1, 1, 1, 2, 2, 3, 3, 5, 6, 6, 6, 8]
        answer = [1, 1, 1, 1, 2, 2, 3, 3, 5, 6, 6, 6, 8]
        result = sort(things)
        self.assertEqual(answer, result)

    def test_decreasing(self):
        sort = self._new()
        things = [7, 6, 6, 5, 2, 1, 1, 0]
        answer = [0, 1, 1, 2, 5, 6, 6, 7]
        result = sort(things)
        self.assertEqual(answer, result)

    def test_all_equal(self):
        sort = self._new()
        things = [7] * 7
        answer = [7] * 7
        result = sort(things)
        self.assertEqual(answer, result)

    def test_with_keys(self):
        sort = self._new()
        things = [
            (4, 7), (7, 0), (0, 5), (1, 5), (5, 3),
            (8, 6), (3, 3), (9, 8), (6, 7), (2, 5),
        ]
        answer = [
            (0, 5), (1, 5), (2, 5), (3, 3), (4, 7),
            (5, 3), (6, 7), (7, 0), (8, 6), (9, 8),
        ]
        result = sort(things, key=lambda x: x[0])
        self.assertEqual(answer, result)
        things = [
            (8, 0), (7, 1), (2, 2), (2, 3), (6, 4),
            (3, 5), (7, 6), (5, 7), (6, 8), (7, 9),
        ]
        answer = [
            (7, 9), (6, 8), (5, 7), (7, 6), (3, 5),
            (6, 4), (2, 3), (2, 2), (7, 1), (8, 0),
        ]
        result = sort(things, key=lambda x: -11.1 * x[1])
        self.assertEqual(answer, result)

    def test_in_place(self):
        sort = self._new()
        things = [4, 1, 4, 2, 5, 7, 7]
        answer = [1, 2, 4, 4, 5, 7, 7]
        result = sort(things)
        self.assertEqual(answer, result)
        if sort is not sorted:
            self.assertIs(things, result)

    def test_instantiate_iterable(self):
        sort = self._new()
        things = range(10)
        answer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = sort(things)
        self.assertEqual(answer, result)

    def test_immutable_indexable(self):
        sort = self._new()
        things = (4, 8, 0, 7, 2, 4, 2)
        answer = [0, 2, 2, 4, 4, 7, 8]
        result = sort(things)
        self.assertEqual(answer, result)


class StableSortTest(SortTest):

    def test_stability(self):
        sort = self._new()
        things = [
            (2, 5), (0, 6), (0, 0), (0, 4), (4, 4),
            (4, 9), (3, 1), (3, 2), (2, 8), (2, 3),
        ]
        answer = [
            (0, 6), (0, 0), (0, 4), (2, 5), (2, 8),
            (2, 3), (3, 1), (3, 2), (4, 4), (4, 9),
        ]
        result = sort(things, key=lambda x: x[0])
        self.assertEqual(answer, result)
