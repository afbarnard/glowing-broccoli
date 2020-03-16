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

def contains(head, item):
    """Return whether the list contains the given item."""
    pass

def count_matches(head, item):
    """
    Return the number of occurrences of the given item in the given
    list.
    """
    pass

def sum(head):
    """Return the sum of all integers in the given list."""
    pass

def get(head, index):
    """Return the item at the specified index."""
    pass

def set(head, index, item):
    """
    Return a list with the item at the specified index replaced with the
    given item.
    """
    pass

def append(head, item):
    """Return a list with the given item added to the end."""
    pass

def extend(head, list):
    """Return a list with the given list added to the end."""
    pass

def insert_at(head, index, item):
    """Return a list with the given item inserted at the given index."""
    pass

def delete_at(head, index):
    """Return a list with the item at the given index deleted."""
    pass

def insert_before(head, new, key):
    """
    Return a list with the new item inserted before the first occurrence
    of the key (if any).
    """
    pass

def delete_before(head, key):
    """
    Return a list with the the item before the first occurrence of the
    key (if any) deleted.
    """
    pass

def insert_after(head, new, key):
    """
    Return a list with the new item inserted after the first occurrence
    of the key (if any).
    """
    pass

def delete_after(head, key):
    """
    Return a list with the item after the first occurrence of the key
    (if any) deleted.
    """
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

def delete_all(head, key):
    """Return a list with all occurrences of the given key deleted."""

def reverse(head):
    """Return a list containing the given items in reverse order."""
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
