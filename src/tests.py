# Generic tests for data structures

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

    def test_empty(self):
        _set = self._new()
        self.assertEqual(0, len(_set))
        for key in KEY_RANGE:
            self.assertNotIn(key, _set)

    def test_len(self):
        _set = self._new(KEY_RANGE)
        self.assertEqual(len(KEY_RANGE), len(_set))

    def test_contains(self):
        _set = self._new(KEY_RANGE)
        for key in KEY_RANGE:
            self.assertIn(key, _set)

    def test_add(self):
        _set = self._new()
        correct = set()
        universe = set(KEY_RANGE)
        for key, value in map_data:
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
        for key, value in map_data:
            correct.add(key)
            _set.add(key)
        # Delete them all!
        for key, value in map_data:
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
