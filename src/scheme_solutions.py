# For practice, implement the following linked list operations as
# recursive functions.  If the name of a function ends in "_tr", its
# implementation should be tail-recursive [1].  Tail recursion is
# important because it is how functional languages implement iteration.
# In such languages, tail recursion is more efficient than plain
# (non-tail) recursion.  Feel free to use helper functions where
# appropriate.  Tail-recursive functions usually need helper functions
# with additional arguments to carry along values before returning them.
#
# These are my recollections on the types of exercises we had to do in
# Scheme [2] for Intro CS at St. Olaf.  In accord with Scheme, all lists
# are chains of (item, next) pairs, where the empty list is (), and no
# iteration is allowed.  Since pairs are immutable in Scheme (and in
# Python), the following functions must all work by building new lists
# out of the old lists.  There is no such thing as modifying the list in
# place.
#
# [1] https://en.wikipedia.org/wiki/Tail_call
# [2] https://en.wikipedia.org/wiki/Scheme_(programming_language)
#
# Implement the solutions to the exercises in a "chapter" and then check
# them by running the tests for that chapter, like this:
#
#     python3 -m unittest scheme_exercises.BasicListQueriesTest

# Copyright (c) 2020 Aubrey Barnard.
#
# This is free, open software licensed under the [MIT License](
# https://choosealicense.com/licenses/mit/).


# Chapter 1
#
# A classic recursive function to start, Fibonacci!  Here, implement the
# naïve, exponentially recursive version, a linear complexity recursive
# version, and a tail-recursive version.  Note that each of these has
# their own test to help get you started.

def fibonacci_exp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_exp(n - 2) + fibonacci_exp(n - 1)

# Check with: python3 -m unittest scheme_exercises.FibonacciExpTest

def fibonacci_rec(n):
    def helper(n):
        if n == 0:
            return (-1, 0)
        elif n == 1:
            return (0, 1)
        else:
            n_2, n_1 = helper(n - 1)
            return (n_1, n_2 + n_1)
    _, n_1 = helper(n)
    return n_1

# Check with: python3 -m unittest scheme_exercises.FibonacciRecTest

def fibonacci_tr(n):
    def helper(n_2, n_1, n):
        if n == 0:
            return n_2
        elif n == 1:
            return n_1
        else:
            return helper(n_1, n_2 + n_1, n - 1)
    return helper(0, 1, n)

# Check with: python3 -m unittest scheme_exercises.FibonacciTrTest


# Chapter 2
#
# Now on to list processing, the bread and butter of recursive functions
# in functional languages such as Lisp / Scheme.  The first function is
# already implemented as an example and as a utility for working with
# the remaining functions.  It converts a Python list to a Scheme-style
# linked list of (item, next) pairs where () is an empty linked list.
# All non-empty linked lists end with an empty linked list.
#
# For example:
#
#     as_pairs([]) -> ()
#     as_pairs([1, 2, 3]) -> (1, (2, (3, ())))
#
# Compare the different implementations.  Make sure you understand the
# different versions, especially how the iterative and tail-recursive
# versions correspond.

def as_pairs_seq(iterable):
    """
    Return the given Python iterable as a sequence of nested (item,
    next) pairs.  No iteration!
    """
    itr = iter(iterable)
    # Use a sentinel object to indicate the end of iteration rather than
    # exception handling because that is more functional in style.
    # Since any object can be an item in the iterable, use the iterator
    # itself as a sentinel object because it is a new object that cannot
    # be an item in the pre-existing iterable.
    head = next(itr, itr)
    # Return an empty list if the iterator is exhausted
    if head is itr:
        return ()
    # Otherwise, return a list with this item as the head
    else:
        return (head, as_pairs_seq(itr))

# If the iterable is actually a Python list ("array") that supports
# random access, then we can do better.  This also demonstrates using a
# helper function.

def as_pairs_ram(array):
    def helper(array, idx, length):
        if idx == length:
            return ()
        else:
            # The head is the item at the current index.  Prepend it to
            # a list containing all of the remaining items.
            return (array[idx], helper(array, idx + 1, length))
    # Call the helper with initial values
    return helper(array, 0, len(array))

# The next function is probably how one would implement `as_pairs`
# iteratively.

def as_pairs_iter(array):
    tail = ()
    for index in range(len(array) - 1, -1, -1):
        head = array[index]
        tail = (head, tail)
    return tail

# The following is a tail-recursive version of the previous.  Examine
# how tail-recursion corresponds to iteration.

def as_pairs_tr_ram(array):
    # Use random access properties to produce a tail-recursive version
    # of the iterative implementation
    def helper(array, index, list):
        if index < 0:
            return list
        else:
            return helper(array, index - 1, (array[index], list))
    return helper(array, len(array) - 1, ())

# What if we need a tail-recursive version that does not depend on
# random access and can handle any iterable?  It's complicated, so don't
# worry if you don't understand this one yet.

def as_pairs_tr_seq(iterable):
    # Use a list to build up the items as a stack in reverse so that
    # they can be popped off in order.
    def backward_helper(stack, list):
        if stack == ():
            return list
        else:
            head, tail = stack
            return backward_helper(tail, (head, list))
    def forward_helper(iterable, stack):
        itr = iter(iterable)
        head = next(itr, itr)
        if head is itr:
            return backward_helper(stack, ())
        else:
            return forward_helper(itr, (head, stack))
    return forward_helper(iterable, ())

# Check with: python3 -m unittest scheme_exercises.AsPairsTest

# Just use the iterative version from now on
as_pairs = as_pairs_iter


# Chapter 3.1: Basic list queries

def length(list):
    """Return the number of items in the list."""
    if list == ():
        return 0
    else:
        _, tail = list
        return 1 + length(tail)

def contains_tr(list, item):
    """
    Return whether the list contains the given item.  (Naturally
    tail-recursive.)
    """
    if list == ():
        return False
    else:
        head, tail = list
        if head == item:
            return True
        else:
            return contains_tr(tail, item)

def count_matches(list, item):
    """
    Return the number of occurrences of the given item in the given
    list.
    """
    if list == ():
        return 0
    else:
        head, tail = list
        if head == item:
            return 1 + count_matches(tail, item)
        else:
            return count_matches(tail, item)

def minimum(ints):
    """
    Return the minimum in a list of integers.  If the list is empty,
    return None.
    """
    if ints == ():
        return None
    else:
        head, tail = ints
        min = minimum(tail)
        if min is None or head <= min:
            return head
        else:
            return min

def sum(list):
    """Return the sum of all integers in the given list."""
    if list == ():
        return 0
    else:
        head, tail = list
        if isinstance(head, int):
            return head + sum(tail)
        else:
            return sum(tail)

def get_tr(list, index):
    """
    Return the item at the specified index.  If the index is out of
    bounds, return an IndexError.  (Naturally tail-recursive.)
    """
    if list == () or index < 0:
        return IndexError()
    else:
        head, tail = list
        if index == 0:
            return head
        else:
            return get_tr(tail, index - 1)

# Check with: python3 -m unittest scheme_exercises.BasicListQueriesTest


# Chapter 3.2: Basic list queries, tail-recursive and alternate versions

def length_tr(list):
    def helper(length, list):
        if list == ():
            return length
        else:
            _, tail = list
            return helper(length + 1, tail)
    return helper(0, list)

def count_matches_tr(list, item):
    def helper(list, item, count):
        if list == ():
            return count
        else:
            head, tail = list
            if head == item:
                return helper(tail, item, count + 1)
            else:
                return helper(tail, item, count)
    return helper(list, item, 0)

def minimum_tr(ints):
    def helper(ints, min):
        if ints == ():
            return min
        else:
            head, tail = ints
            if min is None or head < min:
                return helper(tail, head)
            else:
                return helper(tail, min)
    return helper(ints, None)

def sum_tr(list):
    def helper(list, sum):
        if list == ():
            return sum
        else:
            head, tail = list
            if isinstance(head, int):
                return helper(tail, sum + head)
            else:
                return helper(tail, sum)
    return helper(list, 0)

# Check with: python3 -m unittest scheme_exercises.BasicListQueriesTrTest


# Chapter 4.1: Basic list modifications

def prepend(list, item):
    """
    Return a list with the given item added at the beginning.  (Not
    recursive.)
    """
    return (item, list)

def append(list, item):
    """Return a list with the given item added to the end."""
    if list == ():
        return (item, ())
    else:
        head, tail = list
        return (head, append(tail, item))

def extend(list1, list2):
    """Return a list with the given list added to the end."""
    if list1 == ():
        return list2
    else:
        head, tail = list1
        return (head, extend(tail, list2))

def delete_all(list, key):
    """Return a list with all occurrences of the given key deleted."""
    if list == ():
        return ()
    else:
        head, tail = list
        if head == key:
            return delete_all(tail, key)
        else:
            return (head, delete_all(tail, key))

def reverse_tr(list):
    """
    Return a list containing the given items in reverse order.
    (Naturally tail-recursive.)
    """
    def helper(list, revrsd):
        if list == ():
            return revrsd
        else:
            head, tail = list
            return helper(tail, (head, revrsd))
    return helper(list, ())

# Check with: python3 -m unittest scheme_exercises.BasicListModificationsTest


# Chapter 4.2: Basic list modifications, tail-recursive and alternate  versions

def append_tr(list, item):
    pass

def extend_tr(list1, list2):
    pass

def delete_all_tr(list, key):
    pass

def reverse_nontr(list):
    """
    The easiest and best solution is naturally tail-recursive.  As a
    challenge, implement a non-tail-recursive version.
    """
    pass

# Check with: python3 -m unittest scheme_exercises.BasicListModificationsTrTest


# Chapter 5.1: Intermediate list queries

def find_first(list, key):
    """
    Return the index of the first occurrence of the given key (if any).
    If the key does not occur, return None.
    """
    if list == ():
        return None
    else:
        head, tail = list
        if head == key:
            return 0
        else:
            idx = find_first(tail, key)
            if idx is None:
                return None
            else:
                return idx + 1

def find_last(list, key):
    """
    Return the index of the last occurrence of the given key (if any).
    If the key does not occur, return None.
    """
    if list == ():
        return None
    else:
        head, tail = list
        idx = find_last(tail, key)
        if idx is None:
            if head == key:
                return 0
            else:
                return None
        else:
            return idx + 1

def find_nth(list, key, n):
    """
    Return the index of the n-th occurrence of the given key (if any),
    counting from 1.  If the key does not occur that many times, return
    None.
    """
    if list == () or n < 1:
        return None
    else:
        head, tail = list
        if head == key and n == 1:
            return 0
        else:
            if head == key:
                idx = find_nth(tail, key, n - 1)
            else:
                idx = find_nth(tail, key, n)
            if idx is None:
                return None
            else:
                return idx + 1

# Check with: python3 -m unittest scheme_exercises.IntermediateListQueriesTest


# Chapter 5.2: Intermediate list queries, tail-recursive and alternate versions

def find_first_tr(list, key):
    pass

def find_last_tr(list, key):
    pass

def find_nth_tr(list, key, n):
    pass

# Check with: python3 -m unittest scheme_exercises.IntermediateListQueriesTrTest


# Chapter 6.1: Intermediate list modifications

def set(list, index, item):
    """
    Return a list with the item at the specified index replaced with the
    given item.  If the index is out of bounds, return an IndexError.
    """
    pass

def insert_at(list, index, item):
    """
    Return a list with the given item inserted at the given index.  If
    the index is out of bounds and not just one past the end, return an
    IndexError.
    """
    pass

def delete_at(list, index):
    """
    Return a list with the item at the given index deleted.  If the
    index is out of bounds, return an IndexError.
    """
    pass

def insert_before(list, new, key):
    """
    Return a list with the new item inserted before the first occurrence
    of the key (if any).
    """
    pass

def delete_before(list, key):
    """
    Return a list with the the item before the first occurrence of the
    key (if any) deleted.
    """
    pass

def insert_after(list, new, key):
    """
    Return a list with the new item inserted after the first occurrence
    of the key (if any).
    """
    pass

def delete_after(list, key):
    """
    Return a list with the item after the first occurrence of the key
    (if any) deleted.
    """
    pass

# Check with: python3 -m unittest scheme_exercises.IntermediateListModificationsTest


# Chapter 6.2: Intermediate list modifications, tail-recursive and alternate versions

def set_tr(list, index, item):
    pass

def insert_at_tr(list, index, item):
    pass

def delete_at_tr(list, index):
    pass

def insert_before_tr(list, new, key):
    pass

def delete_before_tr(list, key):
    pass

def insert_after_tr(list, new, key):
    pass

def delete_after_tr(list, key):
    pass

# Check with: python3 -m unittest scheme_exercises.IntermediateListModificationsTrTest


# Chapter 7: Slices and sublists

def get_slice(list, lo, hi):
    """
    Return the sublist that starts at index `lo` and ends at index `hi`
    (inclusive).
    """
    pass

def set_slice(list1, lo, hi, list2):
    """
    Return a list that contains the given list in place of the indicated
    slice (`lo` and `hi` are inclusive).
    """
    pass

def insert_slice(list):
    pass

def delete_slice(list, lo, hi):
    """
    Return a list that omits the given slice (`lo` and `hi` are
    inclusive indices).
    """
    pass

def get_all(list, indices):
    """Return a sublist assembled from the items at the given indices."""
    pass

def del_all(list, indices):
    """Delete all the items at the given indices."""
    pass

def contains_sublist(list, sublist):
    """Return whether the given list contains the given sublist."""
    pass


# Chapter 8: Sorting

def insort_first(list, key):
    pass

def insort_last(list, key):
    pass

def merge_sort(list, compare=None):
    pass


# Chapter 9: Nested lists

def count_nested_matches(list, key):
    """
    Return the number of occurrences of the given key in all of the
    given nested lists.
    """
    pass

def minimum_nested(list):
    """Return the minimum of the integers in the given list."""
    pass

def deepest_level(list):
    """Return the deepest level of nesting of items in the given list.

    For example:

        [] -> 0
        ['a', True, 9.99] -> 1
        [1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]] -> 9
    """
    pass

def flatten(list):
    """
    Given a list possibly containing other lists, flatten them all into
    a single list (in nested traversal order).

    For example:

        flatten([1, 2, [['a', 'b', 'e']], [[12, 21], 32, 23, []]]) ->
            [1, 2, 'a', 'b', 'e', 12, 21, 32, 23]
    """
    pass

def delete_all_all(list, keys):
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
        self.assertEqual((), as_pairs_func([]))
        self.assertEqual(('a', ()), as_pairs_func(['a']))
        self.assertEqual((1, (2, (3, (4, (5, ()))))),
                         as_pairs_func([1, 2, 3, 4, 5]))

    def test_as_pairs_seq(self):
        self._test_as_pairs(as_pairs_seq)

    def test_as_pairs_ram(self):
        self._test_as_pairs(as_pairs_ram)

    def test_as_pairs_iter(self):
        self._test_as_pairs(as_pairs_iter)

    def test_as_pairs_tr_seq(self):
        self._test_as_pairs(as_pairs_tr_seq)

    def test_as_pairs_tr_ram(self):
        self._test_as_pairs(as_pairs_tr_ram)


class _BasicListQueriesTests(unittest.TestCase):

    def length_tests(self, length_func):
        self.assertEqual(0, length_func(as_pairs([])))
        self.assertEqual(1, length_func(as_pairs(['zzz'])))
        self.assertEqual(2, length_func(as_pairs(['baa', 'baa'])))
        self.assertEqual(10, length_func(as_pairs(list(range(100, 110)))))

    def contains_tests(self, contains_func):
        self.assertEqual(False, contains_func(as_pairs([]), 1))
        self.assertEqual(False, contains_func(as_pairs([1]), 2))
        self.assertEqual(False, contains_func(as_pairs([0, 1, 2, 3, 4]), 5))
        self.assertEqual(True, contains_func(as_pairs([1]), 1))
        self.assertEqual(True, contains_func(as_pairs([0, 1, 2, 3, 4]), 4))

    def count_matches_tests(self, count_matches_func):
        self.assertEqual(0, count_matches_func(as_pairs([]), 1))
        self.assertEqual(0, count_matches_func(as_pairs([1]), 2))
        self.assertEqual(0, count_matches_func(as_pairs([0, 1, 2, 3, 4]), 5))
        self.assertEqual(1, count_matches_func(as_pairs([1]), 1))
        self.assertEqual(3, count_matches_func(as_pairs([0, 1, 0, 1, 0]), 0))
        self.assertEqual(111, count_matches_func(as_pairs([1] * 111), 1))

    def minimum_tests(self, minimum_func):
        self.assertEqual(None, minimum_func(as_pairs([])))
        self.assertEqual(-13, minimum_func(as_pairs([-13])))
        self.assertEqual(1, minimum_func(as_pairs([5, 4, 3, 2, 1])))
        self.assertEqual(-5, minimum_func(as_pairs([-5, -4, -3, -2, -1])))
        self.assertEqual(-3, minimum_func(as_pairs([5, 4, -3, -2, -1])))

    def sum_tests(self, sum_func):
        # Zero from empty
        self.assertEqual(0, sum_func(as_pairs([])))
        # Zero from zeros
        self.assertEqual(0, sum_func(as_pairs([0, 0, 0])))
        # Zero from cancellation (include negative numbers!)
        self.assertEqual(0, sum_func(as_pairs(
            [4, 2, -5, -7, 2, 4, 7, 2, -8, -5, 4])))
        # Single number
        self.assertEqual(2, sum_func(as_pairs([2])))
        # Two numbers
        self.assertEqual(5, sum_func(as_pairs([2, 3])))
        # Multiple numbers
        self.assertEqual(77, sum_func(as_pairs(
            [2, 3, 5, 7, 11, 13, 17, 19])))

    def get_tests(self, get_func):
        self.assertIsInstance(get_func(as_pairs([]), 0), IndexError)
        self.assertIsInstance(get_func(as_pairs([1, 2, 3]), -1), IndexError)
        self.assertIsInstance(get_func(as_pairs([1, 2, 3]), 3), IndexError)
        self.assertEqual(3, get_func(as_pairs([3]), 0))
        self.assertEqual(0, get_func(as_pairs([3, 2, 1, 0]), 3))
        self.assertEqual(2, get_func(as_pairs([5, 4, 3, 2, 1]), 3))


class BasicListQueriesTest(_BasicListQueriesTests):

    def test_length(self):
        self.length_tests(length)

    def test_contains_tr(self):
        self.contains_tests(contains_tr)

    def test_count_matches(self):
        self.count_matches_tests(count_matches)

    def test_minimum(self):
        self.minimum_tests(minimum)

    def test_sum(self):
        self.sum_tests(sum)

    def test_get_tr(self):
        self.get_tests(get_tr)


class BasicListQueriesTrTest(_BasicListQueriesTests):

    def test_length_tr(self):
        self.length_tests(length_tr)

    def test_count_matches_tr(self):
        self.count_matches_tests(count_matches_tr)

    def test_minimum_tr(self):
        self.minimum_tests(minimum_tr)

    def test_sum_tr(self):
        self.sum_tests(sum_tr)


class _BasicListModificationsTests(unittest.TestCase):

    def append_tests(self, append_func):
        self.assertEqual(as_pairs([0]), append_func(as_pairs([]), 0))
        self.assertEqual(as_pairs([0, 1]), append_func(as_pairs([0]), 1))
        self.assertEqual(as_pairs([3, 4, 1, 2]),
                         append_func(as_pairs([3, 4, 1]), 2))

    def extend_tests(self, extend_func):
        self.assertEqual(as_pairs([]), extend_func(as_pairs([]), as_pairs([])))
        self.assertEqual(as_pairs([0]), extend_func(as_pairs([0]), as_pairs([])))
        self.assertEqual(as_pairs([1]), extend_func(as_pairs([]), as_pairs([1])))
        self.assertEqual(as_pairs([3, 4, 1, 2]),
                         extend_func(as_pairs([3, 4]), as_pairs([1, 2])))

    def delete_all_tests(self, delete_all_func):
        self.assertEqual(as_pairs(''), delete_all_func(as_pairs(''), 'a'))
        self.assertEqual(as_pairs(''), delete_all_func(as_pairs('aaaaa'), 'a'))
        self.assertEqual(as_pairs('bnn'),
                         delete_all_func(as_pairs('banana'), 'a'))
        self.assertEqual(as_pairs('baaa'),
                         delete_all_func(as_pairs('banana'), 'n'))
        self.assertEqual(as_pairs('banana'),
                         delete_all_func(as_pairs('banana'), 'c'))

    def reverse_tests(self, reverse_func):
        self.assertEqual(as_pairs(''), reverse_func(as_pairs('')))
        self.assertEqual(as_pairs('a'), reverse_func(as_pairs('a')))
        self.assertEqual(as_pairs('tacocat'), reverse_func(as_pairs('tacocat')))


class BasicListModificationsTest(_BasicListModificationsTests):

    def test_prepend(self):
        self.assertEqual(as_pairs([1]), prepend(as_pairs([]), 1))
        self.assertEqual(as_pairs([1, 2, 3]), prepend(as_pairs([2, 3]), 1))

    def test_append(self):
        self.append_tests(append)

    def test_extend(self):
        self.extend_tests(extend)

    def test_delete_all(self):
        self.delete_all_tests(delete_all)

    def test_reverse_tr(self):
        self.reverse_tests(reverse_tr)


class BasicListModificationsTrTest(_BasicListModificationsTests):

    def test_append_tr(self):
        self.append_tests(append_tr)

    def test_extend_tr(self):
        self.extend_tests(extend_tr)

    def test_delete_all_tr(self):
        self.delete_all_tests(delete_all_tr)

    def test_reverse_nontr(self):
        self.reverse_tests(reverse_nontr)


class _IntermediateListQueriesTests(unittest.TestCase):

    def find_first_tests(self, find_first_func):
        self.assertEqual(None, find_first_func(as_pairs([]), 3))
        self.assertEqual(None, find_first_func(as_pairs([1]), 3))
        self.assertEqual(None, find_first_func(as_pairs([2, 4, 6, 8]), 3))
        self.assertEqual(0, find_first_func(as_pairs([3, 3, 3]), 3))
        self.assertEqual(2, find_first_func(as_pairs([1, 2, 3]), 3))
        self.assertEqual(1, find_first_func(as_pairs([1, 0, 0, 0, 1]), 0))

    def find_last_tests(self, find_last_func):
        self.assertEqual(None, find_last_func(as_pairs([]), 3))
        self.assertEqual(None, find_last_func(as_pairs([1]), 3))
        self.assertEqual(None, find_last_func(as_pairs([2, 4, 6, 8]), 3))
        self.assertEqual(2, find_last_func(as_pairs([3, 3, 3]), 3))
        self.assertEqual(0, find_last_func(as_pairs([3, 2, 1]), 3))
        self.assertEqual(3, find_last_func(as_pairs([1, 0, 0, 0, 1]), 0))

    def find_nth_tests(self, find_nth_func):
        self.assertEqual(None, find_nth_func(as_pairs([]), 3, 1))
        self.assertEqual(None, find_nth_func(as_pairs([1]), 3, 1))
        self.assertEqual(None, find_nth_func(as_pairs([2, 4, 6]), 3, 1))
        self.assertEqual(0, find_nth_func(as_pairs([3, 3, 3, 3, 3]), 3, 1))
        self.assertEqual(2, find_nth_func(as_pairs([3, 3, 3, 3, 3]), 3, 3))
        self.assertEqual(4, find_nth_func(as_pairs([3, 3, 3, 3, 3]), 3, 5))
        self.assertEqual(None, find_nth_func(as_pairs([3, 3, 3, 3]), 3, 5))


class IntermediateListQueriesTest(_IntermediateListQueriesTests):

    def test_find_first(self):
        self.find_first_tests(find_first)

    def test_find_last(self):
        self.find_last_tests(find_last)

    def test_find_nth(self):
        self.find_nth_tests(find_nth)


class IntermediateListQueriesTrTest(_IntermediateListQueriesTests):

    def test_find_first_tr(self):
        self.find_first_tests(find_first_tr)

    def test_find_last_tr(self):
        self.find_last_tests(find_last_tr)

    def test_find_nth_tr(self):
        self.find_nth_tests(find_nth_tr)


class _IntermediateListModificationsTests(unittest.TestCase):

    def set_tests(self, set_func):
        self.assertIsInstance(set_func(as_pairs([]), 0, 'a'), IndexError)
        self.assertEqual(as_pairs([2]), set_func(as_pairs([3]), 0, 2))
        self.assertEqual(as_pairs([3, 2, 1, 11]),
                         set_func(as_pairs([3, 2, 1, 0]), 3, 11))
        self.assertEqual(as_pairs([5, 4, 3, 'b', 1]),
                         get_func(as_pairs([5, 4, 3, 2, 1]), 3, 'b'))

    def insert_at_tests(self, insert_at_func):
        self.assertEqual(as_pairs([7]), insert_at_func(as_pairs([]), 0, 7))
        self.assertEqual(as_pairs([0, 1, 2, 3]),
                         insert_at_func(as_pairs([1, 2, 3]), 0, 0))
        self.assertEqual(as_pairs([1, 2, 3, 4]),
                         insert_at_func(as_pairs([1, 2, 3]), 3, 4))
        self.assertEqual(as_pairs([1, 2, 4, 3]),
                         insert_at_func(as_pairs([1, 2, 3]), 2, 4))
        self.assertIsInstance(insert_at_func(as_pairs([0, 1]), 3, 'a'), IndexError)

    def delete_at_tests(self, delete_at_func):
        self.assertEqual(as_pairs([]), delete_at_func(as_pairs([7]), 0))
        self.assertEqual(as_pairs([3, 2, 1]),
                         delete_at_func(as_pairs([4, 3, 2, 1]), 0))
        self.assertEqual(as_pairs([4, 3, 2]),
                         delete_at_func(as_pairs([4, 3, 2, 1]), 3))
        self.assertEqual(as_pairs([4, 2, 1]),
                         delete_at_func(as_pairs([4, 3, 2, 1]), 1))
        self.assertIsInstance(delete_at_func(as_pairs([0, 1]), 2), IndexError)

    def insert_before_tests(self, insert_before_func):
        self.assertEqual(as_pairs(''), insert_before_func(as_pairs(''), 'a', 'b'))
        self.assertEqual(as_pairs('ab'), insert_before_func(as_pairs('b'), 'a', 'b'))
        self.assertEqual(as_pairs('abdcabc'),
                         insert_before_func(as_pairs('abcabc'), 'c', 'd'))
        self.assertEqual(as_pairs('abcde'),
                         insert_before_func(as_pairs('abce'), 'd', 'e'))
        self.assertEqual(as_pairs('abcde'),
                         insert_before_func(as_pairs('abcde'), 'e', 'f'))

    def delete_before_tests(self, delete_before_func):
        self.assertEqual(as_pairs(''), delete_before_func(as_pairs(''), 'a'))
        self.assertEqual(as_pairs('a'), delete_before_func(as_pairs('ba'), 'a'))
        self.assertEqual(as_pairs('ba'), delete_before_func(as_pairs('ba'), 'b'))
        self.assertEqual(as_pairs('abcabc'),
                         delete_before_func(as_pairs('abcabc'), 'd'))
        self.assertEqual(as_pairs('acabc'),
                         delete_before_func(as_pairs('abcabc'), 'c'))

    def insert_after_tests(self, insert_after_func):
        self.assertEqual(as_pairs(''), insert_after_func(as_pairs(''), 'a', 'b'))
        self.assertEqual(as_pairs('aba'), insert_after_func(as_pairs('b'), 'a', 'b'))
        self.assertEqual(as_pairs('abcabc'),
                         insert_after_func(as_pairs('abcabc'), 'c', 'd'))
        self.assertEqual(as_pairs('abcdcba'),
                         insert_after_func(as_pairs('abcdcba'), 'd', 'c'))

    def delete_after_tests(self, delete_after_func):
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


class IntermediateListModificationsTest(_IntermediateListModificationsTests):

    def test_set(self):
        self.set_tests(set)

    def test_insert_at(self):
        self.insert_at_tests(insert_at)

    def test_delete_at(self):
        self.delete_at_tests(delete_at)

    def test_insert_before(self):
        self.insert_before_tests(insert_before)

    def test_delete_before(self):
        self.delete_before_tests(delete_before)

    def test_insert_after(self):
        self.insert_after_tests(insert_after)

    def test_delete_after(self):
        self.delete_after_tests(delete_after)


class IntermediateListModificationsTrTest(_IntermediateListModificationsTests):

    def test_set_tr(self):
        self.set_tests(set_tr)

    def test_insert_at_tr(self):
        self.insert_at_tests(insert_at_tr)

    def test_delete_at_tr(self):
        self.delete_at_tests(delete_at_tr)

    def test_insert_before_tr(self):
        self.insert_before_tests(insert_before_tr)

    def test_delete_before_tr(self):
        self.delete_before_tests(delete_before_tr)

    def test_insert_after_tr(self):
        self.insert_after_tests(insert_after_tr)

    def test_delete_after_tr(self):
        self.delete_after_tests(delete_after_tr)
