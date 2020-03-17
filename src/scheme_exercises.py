# For practice, implement the following linked list operations as both
# (plain) recursive and tail-recursive functions [1].  Use helper functions
# where appropriate.  (Tail-recursive functions usually need helper
# functions with additional arguments to carry along values before
# returning them.)
#
# These are my recollections on the types of exercises we had to do in
# Scheme [2] for Intro CS at St. Olaf.  In accord with Scheme, all lists
# are chains of (item, next) pairs, and no iteration is allowed.  Since
# pairs are immutable in Scheme (and in Python), the following functions
# must all work by building new lists out of the old lists.  There is no
# such thing as modifying the list in place.
#
# [1] https://en.wikipedia.org/wiki/Tail_call
# [2] https://en.wikipedia.org/wiki/Scheme_(programming_language)


# A classic, non-list function to start, Fibonacci!  Here, implement the
# naïve, exponentially recursive version, a linear complexity recursive
# version, and a tail-recursive version.

def fibonacci_exp(n):
    pass

def fibonacci_rec(n):
    pass

def fibonacci_tr(n):
    pass


# Now on to list processing.  The first function is already implemented
# as an example and as a utility for the remaining functions.

def as_pairs(array):
    """
    Return the given Python list ("array") as a sequence of nested
    (item, next) pairs.  No iteration!
    """
    if len(array) == 0:
        return None
    else:
        head = array[0]
        tail = as_pairs(array[1:])
        return (head, tail)

def as_pairs_iter(array):
    # Iterative implementation as a comparison for the tail-recursive
    # implementation
    tail = None
    for index in range(len(array) - 1, -1, -1):
        head = array[index]
        tail = (head, tail)
    return tail

def as_pairs_tr_seq(array):
    # Implement as if array access is sequential and not random access.
    # Use a list to build up the items as a stack in reverse so that
    # they can be popped off in order.
    def backward_helper(stack, list):
        if stack is None:
            return list
        else:
            head, tail = stack
            return backward_helper(tail, (head, list))
    def forward_helper(array, stack):
        if len(array) == 0:
            return backward_helper(stack, None)
        else:
            head = array[0]
            tail = array[1:]
            return forward_helper(tail, (head, stack))
    return forward_helper(array, None)

def as_pairs_tr_ram(array):
    # Use random access properties to produce tail-recursive version of
    # iterative implementation
    def helper(array, index, list):
        if index < 0:
            return list
        else:
            return helper(array, index - 1, (array[index], list))
    return helper(array, len(array) - 1, None)

def length(head):
    """Return the number of items in the list."""
    pass

def length_tr(head):
    pass

def contains(head, item):
    """Return whether the list contains the given item."""
    pass

def contains_tr(head, item):
    pass

def count_matches(head, item):
    """
    Return the number of occurrences of the given item in the given
    list.
    """
    pass

def count_matches_tr(head, item):
    pass

def sum(head):
    """Return the sum of all integers in the given list."""
    pass

def sum_tr(head):
    pass

def get(head, index):
    """
    Return the item at the specified index.  If the index is out of
    bounds, return an IndexError.
    """
    pass

def get_tr(head, index):
    pass

def set(head, index, item):
    """
    Return a list with the item at the specified index replaced with the
    given item.  If the index is out of bounds, return an IndexError.
    """
    pass

def set_tr(head, index, item):
    pass

def append(head, item):
    """Return a list with the given item added to the end."""
    pass

def append_tr(head, item):
    pass

def extend(head, list):
    """Return a list with the given list added to the end."""
    pass

def extend_tr(head, list):
    pass

def insert_at(head, index, item):
    """
    Return a list with the given item inserted at the given index.  If
    the index is out of bounds and not just one past the end, return an
    IndexError.
    """
    pass

def insert_at_tr(head, index, item):
    pass

def delete_at(head, index):
    """
    Return a list with the item at the given index deleted.  If the
    index is out of bounds, return an IndexError.
    """
    pass

def delete_at_tr(head, index):
    pass

def insert_before(head, new, key):
    """
    Return a list with the new item inserted before the first occurrence
    of the key (if any).
    """
    pass

def insert_before_tr(head, new, key):
    pass

def delete_before(head, key):
    """
    Return a list with the the item before the first occurrence of the
    key (if any) deleted.
    """
    pass

def delete_before_tr(head, key):
    pass

def insert_after(head, new, key):
    """
    Return a list with the new item inserted after the first occurrence
    of the key (if any).
    """
    pass

def insert_after_tr(head, new, key):
    pass

def delete_after(head, key):
    """
    Return a list with the item after the first occurrence of the key
    (if any) deleted.
    """
    pass

def delete_after_tr(head, key):
    pass

def delete_all(head, key):
    """Return a list with all occurrences of the given key deleted."""

def delete_all_tr(head, key):
    pass

def reverse(head):
    """Return a list containing the given items in reverse order."""
    pass

def reverse_tr(head):
    pass

def get_slice(head, lo, hi):
    """
    Return the sublist that starts at index `lo` and ends at index `hi`
    (inclusive).
    """
    pass

def set_slice(head, lo, hi, list):
    """
    Return a list that contains the given list in place of the indicated
    slice (`lo` and `hi` are inclusive).
    """
    pass

def insert_slice(head):
    pass

def delete_slice(head, lo, hi):
    """
    Return a list that omits the given slice (`lo` and `hi` are
    inclusive indices).
    """
    pass

def get_all(head, indices):
    """Return a sublist assembled from the items at the given indices."""
    pass

def del_all(head, indices):
    """Delete all the items at the given indices."""
    pass

def contains_sublist(head, sublist):
    """Return whether the given list contains the given sublist."""
    pass


# All right!  Now let's get fancy with nested lists.

def count_nested_matches(head, key):
    """
    Return the number of occurrences of the given key in all of the
    given nested lists.
    """
    pass

def minimum(head):
    """Return the minimum of the integers in the given list."""
    pass

def deepest_level(head):
    """Return the deepest level of nesting of items in the given list.

    For example:

        [] -> 0
        ['a', True, 9.99] -> 1
        [1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]] -> 9
    """
    pass

def flatten(head):
    """
    Given a list possibly containing other lists, flatten them all into
    a single list (in nested traversal order).

    For example:

        flatten([1, 2, [['a', 'b', 'e']], [[12, 21], 32, 23, []]]) ->
            [1, 2, 'a', 'b', 'e', 12, 21, 32, 23]
    """
    pass

def delete_all_all(head, keys):
    """
    Return the given nested lists with all of the occurrences of all of
    the given keys deleted.

    For example:

        delete_all_all([[2], 5, 1, [1, 2, [1, 2], 4, [2, 1]], [[2, 3], 1]], [1, 2]) ->
            [[], 5, [[], 4, []], [[3]]]
    """
    pass


# Tests


import unittest


class FibonacciExpTest(unittest.TestCase):

    # https://oeis.org/A000045/list
    fibonacci_numbers = [
        0, 1, 1, 2, 3,
        5, 8, 13, 21, 34,
        55, 89, 144, 233, 377,
        610, 987, 1597, 2584, 4181,
        6765, 10946, 17711, 28657, 46368,
        75025, 121393, 196418, 317811, 514229,
        832040, 1346269, 2178309, 3524578, 5702887,
        9227465, 14930352, 24157817, 39088169, 63245986,
        102334155,
    ]

    def setUp(self):
        self.fib = fibonacci_exp

    def test_zero_ten(self):
        for idx in range(11):
            fibn = self.fibonacci_numbers[idx]
            with self.subTest(f'fibonacci({idx}) = {fibn}'):
                self.assertEqual(fibn, self.fib(idx))


class FibonacciRecTest(FibonacciExpTest):

    def setUp(self):
        self.fib = fibonacci_rec

    def test_eleven_forty(self):
        for idx in range(11, 41):
            fibn = self.fibonacci_numbers[idx]
            with self.subTest(f'fibonacci({idx}) = {fibn}'):
                self.assertEqual(fibn, self.fib(idx))


class FibonacciTrTest(FibonacciRecTest):

    def setUp(self):
        self.fib = fibonacci_tr


class AsPairsTest(unittest.TestCase):

    def _test_as_pairs(self, as_pairs_func):
        self.assertEqual(None, as_pairs_func([]))
        self.assertEqual(('a', None), as_pairs_func(['a']))
        self.assertEqual((1, (2, (3, None))), as_pairs_func([1, 2, 3]))

    def test_as_pairs_rec(self):
        self._test_as_pairs(as_pairs)

    def test_as_pairs_iter(self):
        self._test_as_pairs(as_pairs_iter)

    def test_as_pairs_tr_seq(self):
        self._test_as_pairs(as_pairs_tr_seq)

    def test_as_pairs_tr_ram(self):
        self._test_as_pairs(as_pairs_tr_ram)


class ListQueriesTest(unittest.TestCase):

    def length_tests(self, length_func):
        as_pairs = as_pairs_iter
        self.assertEqual(0, length_func(as_pairs([])))
        self.assertEqual(1, length_func(as_pairs(['zzz'])))
        self.assertEqual(2, length_func(as_pairs(['baa', 'baa'])))
        self.assertEqual(10, length_func(as_pairs(list(range(100, 110)))))

    def test_length(self):
        self.length_tests(length)

    def test_length_tr(self):
        self.length_tests(length_tr)

    def contains_tests(self, contains_func):
        as_pairs = as_pairs_iter
        self.assertEqual(False, contains_func(as_pairs([]), 1))
        self.assertEqual(False, contains_func(as_pairs([1]), 2))
        self.assertEqual(False, contains_func(as_pairs([0, 1, 2, 3, 4]), 5))
        self.assertEqual(True, contains_func(as_pairs([1]), 1))
        self.assertEqual(True, contains_func(as_pairs([0, 1, 2, 3, 4]), 4))

    def test_contains(self):
        self.contains_tests(contains)

    def test_contains_tr(self):
        self.contains_tests(contains_tr)

    def count_matches_tests(self, count_matches_func):
        as_pairs = as_pairs_iter
        self.assertEqual(0, count_matches_func(as_pairs([]), 1))
        self.assertEqual(0, count_matches_func(as_pairs([1]), 2))
        self.assertEqual(0, contains_func(as_pairs([0, 1, 2, 3, 4]), 5))
        self.assertEqual(1, contains_func(as_pairs([1]), 1))
        self.assertEqual(3, contains_func(as_pairs([0, 1, 0, 1, 0]), 0))
        self.assertEqual(111, contains_func(as_pairs([1] * 111), 1))

    def test_count_matches(self):
        self.count_matches_tests(count_matches)

    def test_count_matches_tr(self):
        self.count_matches_tests(count_matches_tr)

    def sum_tests(self, sum_func):
        as_pairs = as_pairs_iter
        self.assertEqual(0, sum_func(as_pairs([])))
        self.assertEqual(0, sum_func(as_pairs([0])))
        self.assertEqual(2, sum_func(as_pairs([2])))
        self.assertEqual(5, sum_func(as_pairs([2, 3])))
        self.assertEqual(77, sum_func(as_pairs(
            [2, 3, 5, 7, 11, 13, 17, 19])))

    def test_sum(self):
        self.sum_tests(sum)

    def test_sum_tr(self):
        self.sum_tests(sum_tr)

    def get_tests(self, get_func):
        as_pairs = as_pairs_iter
        self.assertIsInstance(get_func(as_pairs([]), 0), IndexError)
        self.assertEqual(3, get_func(as_pairs([3]), 0))
        self.assertEqual(0, get_func(as_pairs([3, 2, 1, 0]), 3))
        self.assertEqual(2, get_func(as_pairs([5, 4, 3, 2, 1]), 3))

    def test_get(self):
        self.get_tests(get)

    def test_get_tr(self):
        self.get_tests(get_tr)


class ListBasicModifyTest(unittest.TestCase):

    def set_tests(self, set_func):
        as_pairs = as_pairs_iter
        self.assertIsInstance(set_func(as_pairs([]), 0, 'a'), IndexError)
        self.assertEqual(as_pairs([2]), set_func(as_pairs([3]), 0, 2))
        self.assertEqual(as_pairs([3, 2, 1, 11]),
                         set_func(as_pairs([3, 2, 1, 0]), 3, 11))
        self.assertEqual(as_pairs([5, 4, 3, 'b', 1]),
                         get_func(as_pairs([5, 4, 3, 2, 1]), 3, 'b'))

    def test_set(self):
        self.set_tests(set)

    def test_set_tr(self):
        self.set_tests(set_tr)

    def append_tests(self, append_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs([0]), append_func(as_pairs([]), 0))
        self.assertEqual(as_pairs([0, 1]), append_func(as_pairs([0]), 1))
        self.assertEqual(as_pairs([3, 4, 1, 2]),
                         append_func(as_pairs([3, 4, 1]), 2))

    def test_append(self):
        self.append_tests(append)

    def test_append_tr(self):
        self.append_tests(append_tr)

    def extend_tests(self, extend_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs([]), extend_func(as_pairs([]), as_pairs([])))
        self.assertEqual(as_pairs([0]), extend_func(as_pairs([0]), as_pairs([])))
        self.assertEqual(as_pairs([1]), extend_func(as_pairs([]), as_pairs([1])))
        self.assertEqual(as_pairs([3, 4, 1, 2]),
                         extend_func(as_pairs([3, 4]), as_pairs([1, 2])))

    def test_extend(self):
        self.extend_tests(extend)

    def test_extend_tr(self):
        self.extend_tests(extend_tr)

    def insert_at_tests(self, insert_at_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs([7]), insert_at_func(as_pairs([]), 0, 7))
        self.assertEqual(as_pairs([0, 1, 2, 3]),
                         insert_at_func(as_pairs([1, 2, 3]), 0, 0))
        self.assertEqual(as_pairs([1, 2, 3, 4]),
                         insert_at_func(as_pairs([1, 2, 3]), 3, 4))
        self.assertEqual(as_pairs([1, 2, 4, 3]),
                         insert_at_func(as_pairs([1, 2, 3]), 2, 4))
        self.assertIsInstance(insert_at_func(as_pairs([0, 1]), 3, 'a'), IndexError)

    def test_insert_at(self):
        self.insert_at_tests(insert_at)

    def test_insert_at_tr(self):
        self.insert_at_tests(insert_at_tr)

    def delete_at_tests(self, delete_at_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs([]), delete_at_func(as_pairs([7]), 0))
        self.assertEqual(as_pairs([3, 2, 1]),
                         delete_at_func(as_pairs([4, 3, 2, 1]), 0))
        self.assertEqual(as_pairs([4, 3, 2]),
                         delete_at_func(as_pairs([4, 3, 2, 1]), 3))
        self.assertEqual(as_pairs([4, 2, 1]),
                         delete_at_func(as_pairs([4, 3, 2, 1]), 1))
        self.assertIsInstance(delete_at_func(as_pairs([0, 1]), 2), IndexError)

    def test_delete_at(self):
        self.delete_at_tests(delete_at)

    def test_delete_at_tr(self):
        self.delete_at_tests(delete_at_tr)

    def insert_before_tests(self, insert_before_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs(''), insert_before_func(as_pairs(''), 'a', 'b'))
        self.assertEqual(as_pairs('ab'), insert_before_func(as_pairs('b'), 'a', 'b'))
        self.assertEqual(as_pairs('abdcabc'),
                         insert_before_func(as_pairs('abcabc'), 'c', 'd'))
        self.assertEqual(as_pairs('abcde'),
                         insert_before_func(as_pairs('abce'), 'd', 'e'))
        self.assertEqual(as_pairs('abcde'),
                         insert_before_func(as_pairs('abcde'), 'e', 'f'))

    def test_insert_before(self):
        self.insert_before_tests(insert_before)

    def test_insert_before_tr(self):
        self.insert_before_tests(insert_before_tr)

    def delete_before_tests(self, delete_before_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs(''), delete_before_func(as_pairs(''), 'a'))
        self.assertEqual(as_pairs('a'), delete_before_func(as_pairs('ba'), 'a'))
        self.assertEqual(as_pairs('ba'), delete_before_func(as_pairs('ba'), 'b'))
        self.assertEqual(as_pairs('abcabc'),
                         delete_before_func(as_pairs('abcabc'), 'd'))
        self.assertEqual(as_pairs('acabc'),
                         delete_before_func(as_pairs('abcabc'), 'c'))

    def test_delete_before(self):
        self.delete_before_tests(delete_before)

    def test_delete_before_tr(self):
        self.delete_before_tests(delete_before_tr)

    def insert_after_tests(self, insert_after_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs(''), insert_after_func(as_pairs(''), 'a', 'b'))
        self.assertEqual(as_pairs('aba'), insert_after_func(as_pairs('b'), 'a', 'b'))
        self.assertEqual(as_pairs('abcabc'),
                         insert_after_func(as_pairs('abcabc'), 'c', 'd'))
        self.assertEqual(as_pairs('abcdcba'),
                         insert_after_func(as_pairs('abcdcba'), 'd', 'c'))

    def test_insert_after(self):
        self.insert_after_tests(insert_after)

    def test_insert_after_tr(self):
        self.insert_after_tests(insert_after_tr)

    def delete_after_tests(self, delete_after_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs(''), delete_after_func(as_pairs(''), 'a'))
        self.assertEqual(as_pairs('ab'), delete_after_func(as_pairs('abc'), 'b'))
        self.assertEqual(as_pairs('abab'),
                         delete_after_func(as_pairs('babab'), 'a'))
        self.assertEqual(as_pairs('abab'),
                         delete_after_func(as_pairs('abcab'), 'b'))
        self.assertEqual(as_pairs('abcde'),
                         delete_after_func(as_pairs('abcde'), 'f'))
        self.assertEqual(as_pairs('abcde'),
                         delete_after_func(as_pairs('abcde'), 'e'))

    def test_delete_after(self):
        self.delete_after_tests(delete_after)

    def test_delete_after_tr(self):
        self.delete_after_tests(delete_after_tr)

    def delete_all_tests(self, delete_all_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs(''), delete_all_func(as_pairs(''), 'a'))
        self.assertEqual(as_pairs(''), delete_all_func(as_pairs('aaaaa'), 'a'))
        self.assertEqual(as_pairs('bnn'),
                         delete_all_func(as_pairs('banana'), 'a'))
        self.assertEqual(as_pairs('baaa'),
                         delete_all_func(as_pairs('banana'), 'n'))
        self.assertEqual(as_pairs('banana'),
                         delete_all_func(as_pairs('banana'), 'c'))

    def test_delete_all(self):
        self.delete_all_tests(delete_all)

    def test_delete_all_tr(self):
        self.delete_all_tests(delete_all_tr)

    def reverse_tests(self, reverse_func):
        as_pairs = as_pairs_iter
        self.assertEqual(as_pairs(''), reverse_func(as_pairs('')))
        self.assertEqual(as_pairs('a'), reverse_func(as_pairs('a')))
        self.assertEqual(as_pairs('tacocat'), reverse_func(as_pairs('tacocat')))

    def test_reverse(self):
        self.reverse_tests(reverse)

    def test_reverse_tr(self):
        self.reverse_tests(reverse_tr)


class ListMultiModifyTest(unittest.TestCase):
    pass


class NestedListsTest(unittest.TestCase):
    pass