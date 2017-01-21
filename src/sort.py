# Practice implementations of various sorting algorithms

import random

from . import tests


def _swap(items, idx1, idx2):
    swap = items[idx1]
    items[idx1] = items[idx2]
    items[idx2] = swap

def _pivot_first(keys, start_idx, stop_idx):
    return start_idx

def _pivot_median_3(keys, start_idx, stop_idx):
    # Get the first, middle, and last keys
    key_first = keys[start_idx]
    middle_idx = (start_idx + stop_idx) // 2
    key_middle = keys[middle_idx]
    last_idx = stop_idx - 1
    key_last = keys[last_idx]
    # Find the median.  Prefer the middle index other things being equal.
    if key_first <= key_middle <= key_last or key_last <= key_middle <= key_first:
        return middle_idx
    elif key_middle <= key_first <= key_last or key_last <= key_first <= key_middle:
        return start_idx
    else:
        return last_idx

def _pivot_random(keys, start_idx, stop_idx):
    idx = random.randrange(start_idx, stop_idx)
    return idx

def _partition_shell(keys, items, start_idx, stop_idx, pivot_idx):
    """Shellsort-like partition function as I remember learning it."""
    # Put the pivot at the end
    last_idx = stop_idx - 1
    pivot_key = keys[pivot_idx]
    if pivot_idx != last_idx:
        _swap(keys, pivot_idx, last_idx)
        if items is not None:
            _swap(items, pivot_idx, last_idx)
    # Partition items based on the pivot.  Items equal to the pivot go
    # in the low partition.  Invariant: lo_idx <= hi_idx.
    lo_idx = start_idx
    hi_idx = last_idx - 1
    while lo_idx <= hi_idx:
        # Leave all keys less than or equal to the pivot in place
        while keys[lo_idx] <= pivot_key and lo_idx < last_idx:
            lo_idx += 1
        # Leave all keys greater than the pivot in place
        while keys[hi_idx] > pivot_key and hi_idx > start_idx:
            hi_idx -= 1
        # Exit early if everything is now on the correct sides of the
        # pivot
        if lo_idx >= hi_idx:
            break
        # Swap lo_idx and hi_idx as they index out-of-order items
        else:
            _swap(keys, lo_idx, hi_idx)
            if items is not None:
                _swap(items, lo_idx, hi_idx)
            lo_idx += 1
            hi_idx -= 1
    # Place the pivot item in its place between the low and high
    # partitions by swapping the last item (the pivot) with the bottom
    # high item
    if lo_idx != last_idx:
        _swap(keys, lo_idx, last_idx)
        if items is not None:
            _swap(items, lo_idx, last_idx)
    # Return the final index of the pivot
    return lo_idx

def _partition_clrsia(keys, items, start_idx, stop_idx, pivot_idx):
    """The partition function from the description of quicksort in Cormen,
    Leiserson, Rivest, and Stein's Introduction to Algorithms.

    """
    # Put the pivot at the end
    last_idx = stop_idx - 1
    pivot_key = keys[pivot_idx]
    if pivot_idx != last_idx:
        _swap(keys, pivot_idx, last_idx)
        if items is not None:
            _swap(items, pivot_idx, last_idx)
    # Partition items based on the pivot.  Items equal to the pivot go
    # in the low partition.  Invariants: low parition:
    # [start_idx:lo_end], high parition: [lo_end:hi_end], start_idx <=
    # lo_end <= hi_end <= last_idx.
    lo_end = start_idx
    for hi_end in range(start_idx, last_idx):
        # Put a low item into place by swapping it with the bottom high
        # item
        if keys[hi_end] <= pivot_key:
            _swap(keys, lo_end, hi_end)
            if items is not None:
                _swap(items, lo_end, hi_end)
            lo_end += 1
    # Place the pivot item in its place between the low and high
    # partitions by swapping the last item (the pivot) with the bottom
    # high item
    if lo_end != last_idx:
        _swap(keys, lo_end, last_idx)
        if items is not None:
            _swap(items, lo_end, last_idx)
    # Return the final index of the pivot
    return lo_end

def _quick(keys, items, start_idx, stop_idx, pick_pivot, partition):
    length = stop_idx - start_idx
    last_idx = stop_idx - 1
    # Base case 1: List of length 1 is already sorted
    if length <= 1:
        return
    # Base case 2: Sort list of length 2 by swapping
    elif length == 2:
        if keys[start_idx] <= keys[last_idx]:
            # Already sorted
            return
        else:
            _swap(keys, start_idx, last_idx)
            if items is not None:
                _swap(items, start_idx, last_idx)
            return
    # List is at least length 3 which is enough to actually do quicksort
    # Pick a pivot
    pivot_idx = pick_pivot(keys, start_idx, stop_idx)
    # Partition items based on the pivot
    pivot_idx = partition(keys, items, start_idx, stop_idx, pivot_idx)
    # Recur on partitions, but only if at least size 2.  It's possible
    # the pivot was first or last resulting in an empty partition.
    # Plus, a partition of size 1 is already sorted.
    if pivot_idx - 1 > start_idx:
        _quick(keys, items, start_idx, pivot_idx, pick_pivot, partition)
    if stop_idx > pivot_idx + 2:
        _quick(keys, items, pivot_idx + 1, stop_idx, pick_pivot, partition)

def quick(items, key=None, pick_pivot=_pivot_median_3, partition=_partition_shell):
    # Instantiate items as a list if not indexable
    if not hasattr(items, '__setitem__') or not hasattr(items, '__getitem__'):
        items = list(items)
    # Items are also keys
    if key is None:
        _quick(items, None, 0, len(items), pick_pivot=pick_pivot, partition=partition)
    # Make keys
    else:
        keys = [key(item) for item in items]
        _quick(keys, items, 0, len(items), pick_pivot=pick_pivot, partition=partition)
    return items


class QuickSortTest_PivotFirst(tests.SortTest):

    def _new(self):
        def sort(items, key=None):
            return quick(items, key, pick_pivot=_pivot_first)
        return sort

class QuickSortTest_PivotMedian3(tests.SortTest):

    def _new(self):
        def sort(items, key=None):
            return quick(items, key, pick_pivot=_pivot_median_3)
        return sort

class QuickSortTest_PivotRandom(tests.SortTest):

    def _new(self):
        def sort(items, key=None):
            return quick(items, key, pick_pivot=_pivot_random)
        return sort

class QuickSortTest_PivotFirst_PartitionClrsia(tests.SortTest):

    def _new(self):
        def sort(items, key=None):
            return quick(items, key, pick_pivot=_pivot_first, partition=_partition_clrsia)
        return sort
