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
    pass

# Check with: python3 -m unittest scheme_exercises.FibonacciExpTest

def fibonacci_rec(n):
    pass

# Check with: python3 -m unittest scheme_exercises.FibonacciRecTest

def fibonacci_tr(n):
    pass

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
    def forward_helper(iterable, stack):
        itr = iter(iterable)
        head = next(itr, itr)
        if head is itr:
            return backward_helper(stack, ())
        else:
            return forward_helper(itr, (head, stack))
    def backward_helper(stack, list):
        if stack == ():
            return list
        else:
            head, tail = stack
            return backward_helper(tail, (head, list))
    return forward_helper(iterable, ())

# Check with: python3 -m unittest scheme_exercises.AsPairsTest

# Just use the iterative version from now on
as_pairs = as_pairs_iter

# Note that, from now on, lists will be written with Python syntax for
# clarity and convenience, but that syntax will actually represent
# linked lists consisting of (item, next) pairs.  This is the way Scheme
# operates: `[1, 2, 3]` is actually just syntactic sugar for `(1, (2,
# (3, ())))`.  Thus, if you want to try out your code, remember to pass
# all Python "arrays" through `as_pairs` first.  For example,
# `length([1, 2, 3, 4])` represents the actual Python code
# `length(as_pairs([1, 2, 3, 4]))`.


# Chapter 3.1: Basic list queries

def length(list):
    """Return the number of items in the list."""
    pass

def contains_tr(list, item):
    """
    Return whether the list contains the given item.  (Naturally
    tail-recursive.)
    """
    pass

def count_matches(list, item):
    """
    Return the number of occurrences of the given item in the given
    list.
    """
    pass

def minimum(ints):
    """
    Return the minimum in a list of integers.  If the list is empty,
    return None.
    """
    pass

def sum(list):
    """Return the sum of all integers in the given list."""
    pass

def get_tr(list, index):
    """
    Return the item at the specified index.  If the index is out of
    bounds, return an IndexError.  (Naturally tail-recursive.)
    """
    pass

# Check with: python3 -m unittest scheme_exercises.BasicListQueriesTest


# Chapter 3.2: Basic list queries, tail-recursive versions

def length_tr(list):
    pass

def count_matches_tr(list, item):
    pass

def minimum_tr(ints):
    pass

def sum_tr(list):
    pass

# Check with: python3 -m unittest scheme_exercises.BasicListQueriesTrTest


# Chapter 4.1: Basic list modifications

def prepend(list, item):
    """
    Return a list with the given item added at the beginning.  (Not
    recursive.)
    """
    pass

def append(list, item):
    """Return a list with the given item added to the end."""
    pass

def extend(list1, list2):
    """Return a list with the given list added to the end."""
    pass

def delete_all(list, key):
    """Return a list with all occurrences of the given key deleted."""
    pass

def reverse_tr(list):
    """
    Return a list containing the given items in reverse order.
    (Naturally tail-recursive.)
    """
    pass

# Check with: python3 -m unittest scheme_exercises.BasicListModificationsTest


# Chapter 4.2: Basic list modifications, tail-recursive and alternate versions

# All Scheme-like linked lists need to be constructed back to front.
# Normally, returning from recursive calls and popping up through the
# call stack provides the mechanism to accomplish this.  Since
# tail-recursive solutions cannot use this mechanism [*], they have to
# provide their own way(s) to construct the expected lists.
#
# [*] Properly tail-recursive languages reuse the top stack frame for a
# tail call rather than pushing a new stack frame.  That means tail
# recursion in such languages is essentially iteration, not recursion!
# But it also means there aren't any new stack frames to pop and so
# functions can't use the call stack as a mechanism for organizing data
# / execution.
#
# The goal with the following exercises is to experiment with the
# tail-recursive approach and experience its benefits / limitations.
#
# Hint: Use `reverse`!

reverse = reverse_tr

def append_tr(list, item):
    pass

def extend_tr(list1, list2):
    pass

def delete_all_tr(list, key):
    pass

def reverse_nontr(list):
    """
    The easiest and best solution is naturally tail-recursive.  As a
    challenge, implement a non-tail-recursive version.  (Hint: Use
    `append`.)  What is the computational complexity compared to
    `reverse_tr`?
    """
    pass

# Check with: python3 -m unittest scheme_exercises.BasicListModificationsTrTest


# Chapter 5.1: Intermediate list queries

def find_first(list, key):
    """
    Return the index of the first occurrence of the given key (if any).
    If the key does not occur, return None.
    """
    pass

def find_last(list, key):
    """
    Return the index of the last occurrence of the given key (if any).
    If the key does not occur, return None.
    """
    pass

def find_nth(list, key, n):
    """
    Return the index of the n-th occurrence of the given key (if any),
    counting from 1.  If the key does not occur that many times, return
    None.
    """
    pass

# Check with: python3 -m unittest scheme_exercises.IntermediateListQueriesTest


# Chapter 5.2: Intermediate list queries, tail-recursive versions

def find_first_tr(list, key):
    pass

def find_last_tr(list, key):
    """Hint: Use two helper functions."""
    pass

def find_nth_tr(list, key, n):
    pass

# Check with: python3 -m unittest scheme_exercises.IntermediateListQueriesTrTest


# Chapter 6.1: Intermediate list modifications

def set(list, index, item):
    """
    Return a list with the item at the specified index replaced with the
    given item.  If the index is out of bounds, return the list unmodified.
    """
    pass

def insert_at(list, index, item):
    """
    Return a list with the given item inserted at the given index.  If
    the index is out of bounds and not just one past the end, return the
    list unmodified.
    """
    pass

def delete_at(list, index):
    """
    Return a list with the item at the given index deleted.  If the
    index is out of bounds, return the list unmodified.
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


# Chapter 6.2: Intermediate list modifications, tail-recursive versions

# Hint: Implement the following helper function.
def prepend_all(stack, list):
    """
    Prepend all of the items in the given stack onto the head of the
    given list.  (Naturally tail-recursive.)

    For example:

        prepend_all([3, 2, 1], [4, 5]) -> [1, 2, 3, 4, 5]
    """
    pass

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


# Chapter 7: Sublists

def sublist_at(list, index, length):
    """
    Return the sublist that starts at the given index and has the given
    length.  If the index is out of bounds, return an empty list.  If
    the length is too long, return only as many item as exist starting
    at `index`.

    For example:

        get_sublist([1, 2, 3, 4, 5], 2, 2) -> [3, 4]
        get_sublist([1, 2, 3, 4, 5], 4, 2) -> [5]
        get_sublist([1, 2, 3, 4, 5], 6, 2) -> []
    """
    pass

def delete_sublist_at(list, index, length):
    """
    Return a list that omits the sublist that starts at the given index
    and has the given length.  If the index is out of bounds, return the
    list unmodified.  If the length is too long, delete only as many
    items as exist starting at `index`.
    """
    pass

def insert_sublist_at(list, index, sublist):
    """
    Return the given list with the given sublist inserted at the given
    index.  If the index is one past the end, append the sublist.  If
    the index is otherwise out of bounds, return the list unmodified.
    """
    pass

def replace_sublist_at(list, index, length, sublist):
    """
    Return a list that contains the given sublist in place of the
    existing sublist that starts at the given index and has the given
    length.  If the index is one past the end, append the sublist.  If
    the index is otherwise out of bounds, return the list unmodified.
    If the length is too long, replace as many items as exist starting
    at `index`.
    """
    pass

def contains_sublist(list, sublist):
    """Return whether the given list contains the given sublist."""
    pass

def select_all(list, indices):
    """
    Return a sublist assembled from the items at the given indices.  If
    an index is out of bounds, ignore it.
    """
    pass

def remove_all(list, indices):
    """
    Remove all the items at the given indices.  If an index is out of
    bounds, ignore it.
    """
    pass

def split(list, index):
    """
    Split the given list into two sublists at the given index and return
    both sublists.  The first sublist should contain items at index 0
    through `index - 1`, and the second sublist should contain the items
    at index `index` through the end.  If the given index is too high,
    return `(list, ())`.
    """
    pass

# Check with: python3 -m unittest scheme_exercises.SublistsTest


# Chapter 8: Sorting

def extract_minimum(list):
    """
    Extract the minimum from the given list of integers and return it
    and the rest of the list as a pair.  If the list is empty, the
    minimum is None.  If the minimum is not unique, extract its first
    occurrence.

    For example:

        extract_minimum([]) -> (None, [])
        extract_minimum([3, 4, 6, 5, 4]) -> (4, [3, 6, 5, 4])
    """
    pass

def selection_sort(list):
    """
    Sort the given list and return it.  Use the selection sort
    algorithm: Extract the minimum, put it at the front, and recur on
    the rest.  Write a stable implementation.
    """
    pass

def insort_first(list, key):
    """
    Insert the given key at its earliest position in sorted order.
    Return the resulting list.
    """
    pass

def insertion_sort(list):
    """
    Sort the given list and return it.  Use the insertion sort
    algorithm: Starting from a sorted list, insert the next element into
    it, and repeat until the whole list is sorted.  Write a stable
    implementation.
    """
    pass

def merge(sorted1, sorted2):
    """Merge two sorted lists into a single sorted list."""
    pass

def merge_sort(list):
    """
    Sort the given list and return it.  Use the merge sort algorithm:
    Split the list into two halves, sort the first half, sort the second
    half, then merge the two halves.  Write a stable implementation.
    """
    pass

def iterable_sort(list):
    """
    Optional: As a challenge, write a version of merge sort that works
    for iterables.  That is, it can't use `length` or `split` and must
    look at the list one (head, tail) pair at a time.
    """
    pass

# Check with: python3 -m unittest scheme_exercises.SortingTest


# Chapter 9: Nested lists

# Working with nested lists requires two additional pieces of machinery.
# The first is a predicate to tell when an item is a list and needs
# recursive processing, and the second is a version of `as_pairs` that
# can handle nested lists.  The latter will be needed to convert nested
# Python lists into nested Scheme-style linked lists, and also serves as
# a good example of how to do recursive programming with nested lists.

def is_list(obj):
    if obj == ():
        return True
    else:
        return (isinstance(obj, tuple) and
                len(obj) == 2 and is_list(obj[1]))

def nested_as_pairs(iterable):
    itr = iter(iterable)
    head = next(itr, itr)
    if head is itr:
        return ()
    # Instead of the following `isinstance` which tests for Python
    # lists, your code should use `is_list` to test for Scheme-style
    # linked lists.
    elif isinstance(head, list):
        return (nested_as_pairs(head), nested_as_pairs(itr))
    else:
        return (head, nested_as_pairs(itr))

def count_nested_matches(list, key):
    """
    Return the number of occurrences of the given key in all of the
    given nested lists.
    """
    pass

def minimum_nested(list):
    """
    Return the minimum of the integers in the given list.  If there are
    no integers, then the minimum is None.
    """
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

# Check with: python3 -m unittest scheme_exercises.NestedListsTest


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
        self.assertEqual(as_pairs([2]), set_func(as_pairs([3]), 0, 2))
        self.assertEqual(as_pairs([3, 2, 1, 11]),
                         set_func(as_pairs([3, 2, 1, 0]), 3, 11))
        self.assertEqual(as_pairs([5, 4, 3, 'b', 1]),
                         set_func(as_pairs([5, 4, 3, 2, 1]), 3, 'b'))
        self.assertEqual(as_pairs([]),
                         set_func(as_pairs([]), 0, 'a'))
        self.assertEqual(as_pairs([1, 2, 3]),
                         set_func(as_pairs([1, 2, 3]), -1, 0))

    def insert_at_tests(self, insert_at_func):
        self.assertEqual(as_pairs([7]), insert_at_func(as_pairs([]), 0, 7))
        self.assertEqual(as_pairs([0, 1, 2, 3]),
                         insert_at_func(as_pairs([1, 2, 3]), 0, 0))
        self.assertEqual(as_pairs([1, 2, 3, 4]),
                         insert_at_func(as_pairs([1, 2, 3]), 3, 4))
        self.assertEqual(as_pairs([1, 2, 4, 3]),
                         insert_at_func(as_pairs([1, 2, 3]), 2, 4))
        self.assertEqual(as_pairs([0, 1]),
                         insert_at_func(as_pairs([0, 1]), 3, 'a'))
        self.assertEqual(as_pairs([0, 1]),
                         insert_at_func(as_pairs([0, 1]), -1, 'a'))

    def delete_at_tests(self, delete_at_func):
        self.assertEqual(as_pairs([]), delete_at_func(as_pairs([7]), 0))
        self.assertEqual(as_pairs([3, 2, 1]),
                         delete_at_func(as_pairs([4, 3, 2, 1]), 0))
        self.assertEqual(as_pairs([4, 3, 2]),
                         delete_at_func(as_pairs([4, 3, 2, 1]), 3))
        self.assertEqual(as_pairs([4, 2, 1]),
                         delete_at_func(as_pairs([4, 3, 2, 1]), 1))
        self.assertEqual(as_pairs([0, 1]),
                         delete_at_func(as_pairs([0, 1]), 2))

    def insert_before_tests(self, insert_before_func):
        # Empty
        self.assertEqual(as_pairs(''),
                         insert_before_func(as_pairs(''), 'z', 'a'))
        # Insert before first
        self.assertEqual(as_pairs('zabc'),
                         insert_before_func(as_pairs('abc'), 'z', 'a'))
        # Insert before middle
        self.assertEqual(as_pairs('azbc'),
                         insert_before_func(as_pairs('abc'), 'z', 'b'))
        # Insert before last
        self.assertEqual(as_pairs('abzc'),
                         insert_before_func(as_pairs('abc'), 'z', 'c'))
        # Key not found
        self.assertEqual(as_pairs('abc'),
                         insert_before_func(as_pairs('abc'), 'z', 'd'))
        # Insert before first of multiple
        self.assertEqual(as_pairs('brook'),
                         insert_before_func(as_pairs('book'), 'r', 'o'))

    def delete_before_tests(self, delete_before_func):
        # Delete from empty
        self.assertEqual(as_pairs(''),
                         delete_before_func(as_pairs(''), 'a'))
        # Delete before beginning
        self.assertEqual(as_pairs('abcde'),
                         delete_before_func(as_pairs('abcde'), 'a'))
        # Delete at beginning
        self.assertEqual(as_pairs('bcde'),
                         delete_before_func(as_pairs('abcde'), 'b'))
        # Delete from middle
        self.assertEqual(as_pairs('abde'),
                         delete_before_func(as_pairs('abcde'), 'd'))
        # Delete at end
        self.assertEqual(as_pairs('abce'),
                         delete_before_func(as_pairs('abcde'), 'e'))
        # Key not found
        self.assertEqual(as_pairs('abcde'),
                         delete_before_func(as_pairs('abcde'), 'f'))
        # Delete before first when multiple
        self.assertEqual(as_pairs('baba'),
                         delete_before_func(as_pairs('ababa'), 'b'))

    def insert_after_tests(self, insert_after_func):
        # Empty
        self.assertEqual(as_pairs(''),
                         insert_after_func(as_pairs(''), 'z', 'a'))
        # Insert after first
        self.assertEqual(as_pairs('azbc'),
                         insert_after_func(as_pairs('abc'), 'z', 'a'))
        # Insert after middle
        self.assertEqual(as_pairs('abzc'),
                         insert_after_func(as_pairs('abc'), 'z', 'b'))
        # Insert after last
        self.assertEqual(as_pairs('abcz'),
                         insert_after_func(as_pairs('abc'), 'z', 'c'))
        # Key not found
        self.assertEqual(as_pairs('abc'),
                         insert_after_func(as_pairs('abc'), 'z', 'd'))
        # Insert after first of multiple
        self.assertEqual(as_pairs('bozo'),
                         insert_after_func(as_pairs('boo'), 'z', 'o'))

    def delete_after_tests(self, delete_after_func):
        # Delete from empty
        self.assertEqual(as_pairs(''),
                         delete_after_func(as_pairs(''), 'a'))
        # Delete at beginning
        self.assertEqual(as_pairs('acde'),
                         delete_after_func(as_pairs('abcde'), 'a'))
        # Delete from middle
        self.assertEqual(as_pairs('abde'),
                         delete_after_func(as_pairs('abcde'), 'b'))
        # Delete at end
        self.assertEqual(as_pairs('abcd'),
                         delete_after_func(as_pairs('abcde'), 'd'))
        # Delete after end
        self.assertEqual(as_pairs('abcde'),
                         delete_after_func(as_pairs('abcde'), 'e'))
        # Key not found
        self.assertEqual(as_pairs('abcde'),
                         delete_after_func(as_pairs('abcde'), 'f'))
        # Delete after first when multiple
        self.assertEqual(as_pairs('abba'),
                         delete_after_func(as_pairs('ababa'), 'b'))


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


class SublistsTest(unittest.TestCase):

    def test_sublist_at(self):
        # Empty list
        self.assertEqual(as_pairs(''), sublist_at(as_pairs(''), 0, 1))
        # Zero length
        self.assertEqual(as_pairs(''), sublist_at(as_pairs('123'), 0, 0))
        # Bad length
        self.assertEqual(as_pairs(''), sublist_at(as_pairs('123'), 1, -1))
        # Sliding window (includes indices out of bounds)
        self.assertEqual(as_pairs(''), sublist_at(as_pairs('123'), -1, 2))
        self.assertEqual(as_pairs('12'), sublist_at(as_pairs('123'), 0, 2))
        self.assertEqual(as_pairs('23'), sublist_at(as_pairs('123'), 1, 2))
        self.assertEqual(as_pairs('3'), sublist_at(as_pairs('123'), 2, 2))
        self.assertEqual(as_pairs(''), sublist_at(as_pairs('123'), 3, 2))
        # Whole list
        self.assertEqual(as_pairs('123'), sublist_at(as_pairs('123'), 0, 3))

    def delete_sublist_at_tests(self, dlt):
        # Empty list
        self.assertEqual(as_pairs(''), dlt(as_pairs(''), 0, 1))
        # Zero length
        self.assertEqual(as_pairs('123'), dlt(as_pairs('123'), 0, 0))
        # Bad length
        self.assertEqual(as_pairs('123'), dlt(as_pairs('123'), 1, -1))
        # Sliding window (includes indices out of bounds)
        self.assertEqual(as_pairs('123'), dlt(as_pairs('123'), -1, 2))
        self.assertEqual(as_pairs('3'), dlt(as_pairs('123'), 0, 2))
        self.assertEqual(as_pairs('1'), dlt(as_pairs('123'), 1, 2))
        self.assertEqual(as_pairs('12'), dlt(as_pairs('123'), 2, 2))
        self.assertEqual(as_pairs('123'), dlt(as_pairs('123'), 3, 2))
        # Whole list
        self.assertEqual(as_pairs(''), dlt(as_pairs('123'), 0, 3))

    def test_delete_sublist_at(self):
        self.delete_sublist_at_tests(delete_sublist_at)

    def insert_sublist_at_tests(self, ins):
        # Empty lists
        self.assertEqual(as_pairs(''), ins(as_pairs(''), 0, as_pairs('')))
        self.assertEqual(as_pairs('x'), ins(as_pairs(''), 0, as_pairs('x')))
        self.assertEqual(as_pairs('a'), ins(as_pairs('a'), 0, as_pairs('')))
        # Insert at beginning
        self.assertEqual(as_pairs('xyabc'), ins(as_pairs('abc'), 0, as_pairs('xy')))
        # Insert in middle
        self.assertEqual(as_pairs('abxyc'), ins(as_pairs('abc'), 2, as_pairs('xy')))
        # Insert at end
        self.assertEqual(as_pairs('abcxy'), ins(as_pairs('abc'), 3, as_pairs('xy')))
        # Indices out of bounds
        self.assertEqual(as_pairs('abc'), ins(as_pairs('abc'), -1, as_pairs('xy')))
        self.assertEqual(as_pairs('abc'), ins(as_pairs('abc'), 4, as_pairs('xy')))

    def test_insert_sublist_at(self):
        self.insert_sublist_at_tests(insert_sublist_at)

    def test_replace_sublist_at(self):
        rpl = replace_sublist_at
        # Do deletion tests
        self.delete_sublist_at_tests(lambda l, i, s: rpl(l, i, s, ()))
        # Do insertion tests
        self.insert_sublist_at_tests(lambda l, i, s: rpl(l, i, 0, s))
        # Replace at beginning
        self.assertEqual(as_pairs('xyz2345'),
                         rpl(as_pairs('12345'), 0, 1, as_pairs('xyz')))
        self.assertEqual(as_pairs('xyz45'),
                         rpl(as_pairs('12345'), 0, 3, as_pairs('xyz')))
        self.assertEqual(as_pairs('xyz'),
                         rpl(as_pairs('12345'), 0, 5, as_pairs('xyz')))
        # Replace in middle
        self.assertEqual(as_pairs('1xyz5'),
                         rpl(as_pairs('12345'), 1, 3, as_pairs('xyz')))
        self.assertEqual(as_pairs('12xyz45'),
                         rpl(as_pairs('12345'), 2, 1, as_pairs('xyz')))
        # Replace at end
        self.assertEqual(as_pairs('12xyz'),
                         rpl(as_pairs('12345'), 2, 4, as_pairs('xyz')))
        self.assertEqual(as_pairs('12345xyz'),
                         rpl(as_pairs('12345'), 5, 3, as_pairs('xyz')))
        # Indices out of bounds
        self.assertEqual(as_pairs('12345'),
                         rpl(as_pairs('12345'), -1, 5, as_pairs('xyz')))
        self.assertEqual(as_pairs('12345'),
                         rpl(as_pairs('12345'), 6, 6, as_pairs('xyz')))

    def test_contains_sublist(self):
        ctn = contains_sublist
        # Empty doesn't contain anything except empty
        self.assertEqual(False, ctn(as_pairs(''), as_pairs('xyz')))
        self.assertEqual(True, ctn(as_pairs(''), as_pairs('')))
        # Everything contains empty
        self.assertEqual(True, ctn(as_pairs('abc'), as_pairs('')))
        # Sublist length 1
        self.assertEqual(True, ctn(as_pairs('abc'), as_pairs('a')))
        self.assertEqual(True, ctn(as_pairs('abc'), as_pairs('c')))
        self.assertEqual(False, ctn(as_pairs('abc'), as_pairs('x')))
        # Sublist length 2
        self.assertEqual(True, ctn(as_pairs('abc'), as_pairs('ab')))
        self.assertEqual(True, ctn(as_pairs('abc'), as_pairs('bc')))
        self.assertEqual(False, ctn(as_pairs('abc'), as_pairs('ac')))
        # Contains self
        self.assertEqual(True, ctn(as_pairs('abc'), as_pairs('abc')))
        self.assertEqual(False, ctn(as_pairs('abc'), as_pairs('abcd')))

    def test_select_all(self):
        self.assertEqual(as_pairs(''), select_all(
            as_pairs('abcdefghijklm'), as_pairs([])))
        self.assertEqual(as_pairs(''), select_all(
            as_pairs(''), as_pairs([3, 1, 2, 0])))
        self.assertEqual(as_pairs(''), select_all(
            as_pairs('abc'), as_pairs([3, 4, 5])))
        self.assertEqual(as_pairs('abc'), select_all(
            as_pairs('abc'), as_pairs([0, 1, 2])))
        self.assertEqual(as_pairs('cdfil'), select_all(
            as_pairs('abcdefghijklm'), as_pairs([2, 3, 5, 8, 11])))
        self.assertEqual(as_pairs('feedface'), select_all(
            as_pairs('abcdef'), as_pairs([5, 4, 4, 3, 5, 0, 2, 4])))
        self.assertEqual(as_pairs('aaccee'), select_all(
            as_pairs('abcdef'), as_pairs([0, 0, 2, 2, 4, 4])))

    def test_remove_all(self):
        self.assertEqual(as_pairs('abc'), remove_all(
            as_pairs('abc'), as_pairs([])))
        self.assertEqual(as_pairs(''), remove_all(
            as_pairs(''), as_pairs([3, 1, 2, 0])))
        self.assertEqual(as_pairs('abc'), remove_all(
            as_pairs('abc'), as_pairs([3, 4, 5])))
        self.assertEqual(as_pairs(''), remove_all(
            as_pairs('abc'), as_pairs([0, 1, 2])))
        self.assertEqual(as_pairs('abeghjkm'), remove_all(
            as_pairs('abcdefghijklm'), as_pairs([2, 3, 5, 8, 11])))
        self.assertEqual(as_pairs('b'), remove_all(
            as_pairs('abcdef'), as_pairs([5, 4, 4, 3, 5, 0, 2, 4])))
        self.assertEqual(as_pairs('ace'), remove_all(
            as_pairs('abcdef'), as_pairs([1, 1, 3, 3, 5, 5])))

    def test_split(self):
        self.assertEqual((as_pairs([]), as_pairs([])),
                         split(as_pairs([]), 1))
        self.assertEqual((as_pairs([]), as_pairs([1, 2, 3])),
                         split(as_pairs([1, 2, 3]), 0))
        self.assertEqual((as_pairs([1, 2, 3]), as_pairs([])),
                         split(as_pairs([1, 2, 3]), 3))
        self.assertEqual((as_pairs([1]), as_pairs([2, 3, 4, 5])),
                         split(as_pairs([1, 2, 3, 4, 5]), 1))
        self.assertEqual((as_pairs([1, 2, 3, 4]), as_pairs([5])),
                         split(as_pairs([1, 2, 3, 4, 5]), 4))


class SortingTest(unittest.TestCase):

    def test_extract_minimum(self):
        self.assertEqual(as_pairs([None]), extract_minimum(as_pairs([])))
        self.assertEqual(as_pairs([4]), extract_minimum(as_pairs([4])))
        self.assertEqual(as_pairs([-4, 8]), extract_minimum(as_pairs([-4, 8])))
        self.assertEqual(as_pairs([-4, 8]), extract_minimum(as_pairs([8, -4])))
        self.assertEqual(as_pairs([1, 2, 2]), extract_minimum(as_pairs([2, 1, 2])))
        self.assertEqual(as_pairs([-7, 4, 4, -4, 2, 1, 4, -7]),
                         extract_minimum(as_pairs([4, 4, -4, 2, 1, -7, 4, -7])))

    def sort_tests(self, sort_func):
        self.assertEqual(as_pairs([]), sort_func(as_pairs([])))
        self.assertEqual(as_pairs([1]), sort_func(as_pairs([1])))
        self.assertEqual(as_pairs([-3, -2, -1]),
                         sort_func(as_pairs([-3, -2, -1])))
        self.assertEqual(as_pairs([1, 2, 3, 4, 5]),
                         sort_func(as_pairs([5, 4, 3, 2, 1])))
        self.assertEqual(as_pairs([0, 1, 1, 1, 1, 1, 1]),
                         sort_func(as_pairs([1, 1, 1, 1, 1, 1, 0])))
        self.assertEqual(
            as_pairs(
                [-9, -7, -7, -7, -4, -3, -2, 0, 1, 2, 6, 6, 7, 7, 8, 9, 9]),
            sort_func(as_pairs(
                [9, 7, -4, 2, -9, 9, 7, 0, 8, -3, 6, -7, -2, -7, 1, -7, 6])))

    def test_selection_sort(self):
        self.sort_tests(selection_sort)

    def test_insort_first(self):
        self.assertEqual(as_pairs([0]), insort_first(as_pairs([]), 0))
        self.assertEqual(as_pairs([0, 0]), insort_first(as_pairs([0]), 0))
        self.assertEqual(as_pairs([0, 1]), insort_first(as_pairs([0]), 1))
        self.assertEqual(as_pairs([0, 1]), insort_first(as_pairs([1]), 0))
        # Insort at beginning
        self.assertEqual(as_pairs([-4, -4, -3, 0, 1, 3, 4, 8]),
                         insort_first(as_pairs([-4, -3, 0, 1, 3, 4, 8]), -4))
        self.assertEqual(as_pairs([-4, -3, -3, 0, 1, 3, 4, 8]),
                         insort_first(as_pairs([-4, -3, 0, 1, 3, 4, 8]), -3))
        # Insort at end
        self.assertEqual(as_pairs([-4, -3, 0, 1, 3, 4, 7, 8]),
                         insort_first(as_pairs([-4, -3, 0, 1, 3, 4, 8]), 7))
        self.assertEqual(as_pairs([-4, -3, 0, 1, 3, 4, 8, 8]),
                         insort_first(as_pairs([-4, -3, 0, 1, 3, 4, 8]), 8))
        self.assertEqual(as_pairs([-4, -3, 0, 1, 3, 4, 8, 9]),
                         insort_first(as_pairs([-4, -3, 0, 1, 3, 4, 8]), 9))

    def test_insertion_sort(self):
        self.sort_tests(insertion_sort)

    def test_merge(self):
        self.assertEqual(as_pairs([]), merge(as_pairs([]), as_pairs([])))
        self.assertEqual(as_pairs([0]), merge(as_pairs([0]), as_pairs([])))
        self.assertEqual(as_pairs([0]), merge(as_pairs([]), as_pairs([0])))
        self.assertEqual(as_pairs([0, 0]), merge(as_pairs([0]), as_pairs([0])))
        self.assertEqual(as_pairs([0, 1]), merge(as_pairs([0]), as_pairs([1])))
        self.assertEqual(as_pairs([0, 1]), merge(as_pairs([1]), as_pairs([0])))
        self.assertEqual(
            as_pairs(list(range(10))),
            merge(
                as_pairs([1, 3, 5, 7, 9]),
                as_pairs([0, 2, 4, 6, 8])))
        self.assertEqual(
            as_pairs(list(range(12))),
            merge(
                as_pairs([0, 1, 2, 3, 4, 6, 8]),
                as_pairs([5, 7, 9, 10, 11])))
        self.assertEqual(
            as_pairs([-5, -5, -3, -2, -1, 1, 5, 5, 8, 9]),
            merge(
                as_pairs([-5, -2, 1, 8, 9]),
                as_pairs([-5, -3, -1, 5, 5])))

    def test_merge_sort(self):
        self.sort_tests(merge_sort)

    def test_iterable_sort(self):
        # Only run this test if it has been implemented.  All functions
        # whose body is only "return <value>" appear to have a byte code
        # length of 4 and anything more complicated is longer (including
        # "return <call>").
        if len(iterable_sort.__code__.co_code) > 4:
            self.sort_tests(iterable_sort)


class NestedListsInfrastructureTest(unittest.TestCase):

    def test_is_list(self):
        self.assertEqual(True, is_list(()))
        self.assertEqual(True, is_list(('a', ())))
        self.assertEqual(False, is_list(('a', 'b')))
        self.assertEqual(True, is_list((('a', ()), ('b', ('c', ())))))
        self.assertEqual(False, is_list((('a', ()), ('b', ('c', None)))))
        self.assertEqual(False, is_list([]))
        self.assertEqual(False, is_list((0, 1, 2)))
        self.assertEqual(False, is_list((0,)))

    def test_nested_as_pairs(self):
        nap = nested_as_pairs
        # Empty
        self.assertEqual((), nap([]))
        # Sequence
        self.assertEqual(
            ((), ((), ((), ((), ((), ()))))),
            nap([[], [], [], [], []]))
        # Nested
        self.assertEqual(
            (((((), ()), ()), ()), ()),
            nap([[[[[]]]]]))
        # Nested + sequence
        self.assertEqual(
            (((), ()), (((), ((), ())), ())),
            nap([[[]], [[], []]]))
        # With other items
        self.assertEqual(
            (1, ((2, (((4, ()), ()), ())), (((3, ()), ()), ()))),
            nap([1, [2, [[4]]], [[3]]]))


class NestedListsTest(unittest.TestCase):

    def test_count_nested_matches(self):
        nap = nested_as_pairs
        self.assertEqual(0, count_nested_matches(nap([]), 1))
        self.assertEqual(0, count_nested_matches(nap([0]), 1))
        self.assertEqual(1, count_nested_matches(nap([0]), 0))
        self.assertEqual(7, count_nested_matches(
            nap([[[[[[5, 0], 4, 0], 3, 0], 2, 0], 1, 0], 0, 0]), 0))
        self.assertEqual(7, count_nested_matches(
            nap([0, 0, [1, 0, [2, 0, [3, 0, [4, 0, [5, 0]]]]]]), 0))
        self.assertEqual(4, count_nested_matches(
            nap(['000', (0, 0, 0), [0, 0, 0, ['0', (0,), [0]]]]), 0))

    def test_minimum_nested(self):
        nap = nested_as_pairs
        self.assertEqual(None, minimum_nested(nap([])))
        self.assertEqual(None, minimum_nested(nap('abcde')))
        self.assertEqual(1, minimum_nested(
            nap(['a', (0,), [['b'], 1], 2, 'c'])))
        self.assertEqual(-5, minimum_nested(
            nap([[0], [0, [-1]], [0, [-1, [-2]]],
                 [0, [-1, [-2, [-3, [-4, [-5]]]]]]])))
        self.assertEqual(-10, minimum_nested(
            nap([0, [-1, [-2, [-3, [-4, [-5], -6], -7], -8], -9], -10])))

    def test_deepest_level(self):
        nap = nested_as_pairs
        self.assertEqual(0, deepest_level(nap([])))
        self.assertEqual(0, deepest_level(nap([[[]]])))
        self.assertEqual(1, deepest_level(nap(['a', True, 9.99])))
        self.assertEqual(9, deepest_level(
            nap([1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]])))
        self.assertEqual(5, deepest_level(
            nap(['a', ['b'], [['c']], [[['d']]], [[[['e']]]]])))
        self.assertEqual(5, deepest_level(
            nap(['a', ['b'], [['c']], [[['d']]], [[[['e']]]],
                 [[[[[]]]]]])))

    def test_flatten(self):
        nap = nested_as_pairs
        self.assertEqual(nap([]), flatten(nap([])))
        self.assertEqual(nap([]), flatten(
            nap([[[[[], []], []], []], [[], [[], [[], []]]]])))
        self.assertEqual(nap(range(4)), flatten(
            nap([[[[[0], [1]], []], []], [[], [[], [[2], [3]]]]])))
        self.assertEqual(
            nap([1, (2, []), 'a', 'b', 'e', 12, 21, 32, 23]),
            flatten(nap([1, (2, []), [['a', 'b', 'e']], [[12, 21], 32, 23, []]])))

    def test_delete_all_all(self):
        nap = nested_as_pairs
        daa = delete_all_all
        self.assertEqual(nap([]), daa(nap([]), nap(range(10))))
        self.assertEqual(nap(range(10)), daa(nap(range(10)), nap([])))
        self.assertEqual(nap([]), daa(nap(range(10)), nap(range(10))))
        self.assertEqual(
            nap([[], 5, [[], 4, []], [[3]]]),
            daa(nap([[2], 5, 1, [1, 2, [1, 2], 4, [2, 1]], [[2, 3], 1]]),
                nap([1, 2])))
