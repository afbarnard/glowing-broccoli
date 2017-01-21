# Practice implementations of various sorting algorithms

import random

from . import tests


def _swap(items, idx1, idx2):
    swap = items[idx1]
    items[idx1] = items[idx2]
    items[idx2] = swap

def _pivot_first(keys, start_idx, stop_idx):
    return start_idx, keys[start_idx]

def _pivot_median_3(keys, start_idx, stop_idx):
    # Get the first, middle, and last keys
    key_first = keys[start_idx]
    middle_idx = (start_idx + stop_idx) // 2
    key_middle = keys[middle_idx]
    last_idx = stop_idx - 1
    key_last = keys[last_idx]
    # Find the median.  Prefer the middle index other things being equal.
    if key_first <= key_middle <= key_last or key_last <= key_middle <= key_first:
        return middle_idx, key_middle
    elif key_middle <= key_first <= key_last or key_last <= key_first <= key_middle:
        return start_idx, key_first
    else:
        return last_idx, key_last

def _pivot_random(keys, start_idx, stop_idx):
    idx = random.randrange(start_idx, stop_idx)
    return idx, keys[idx]

def _quick(keys, items, start_idx, stop_idx, pick_pivot):
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
    pivot_idx, pivot_key = pick_pivot(keys, start_idx, stop_idx)
    if items is not None:
        pivot_item = items[pivot_idx]
    # Partition items based on the pivot.  Items equal to the pivot go
    # in the low partition.  Invariant: lo_idx <= empty_idx <= hi_idx.
    empty_idx = pivot_idx
    lo_idx = start_idx
    hi_idx = last_idx
    while lo_idx < hi_idx:
        # Leave all keys less than or equal to the pivot in place
        while keys[lo_idx] <= pivot_key and lo_idx < empty_idx:
            lo_idx += 1
        # Leave all keys greater than the pivot in place
        while keys[hi_idx] > pivot_key and hi_idx > empty_idx:
            hi_idx -= 1
        # Done.  Everything was already on the correct sides of the pivot.
        if lo_idx == empty_idx == hi_idx:
            continue
        # Move the empty slot to keep it in the middle
        elif lo_idx == empty_idx or hi_idx == empty_idx:
            # Put the empty slot in the middle unless hi_idx - lo_idx ==
            # 1 in which case the empty and the non-empty slots need to
            # be swapped (because if the non-empty key was already on
            # the correct side of the pivot then lo_idx == empty_idx ==
            # hi_idx and the case above would have been taken)
            middle_idx = (lo_idx + hi_idx) // 2
            if lo_idx == empty_idx and hi_idx - lo_idx == 1:
                # Change the middle from lo_idx to hi_idx so that a swap
                # takes place
                middle_idx = hi_idx
            # "Swap" empty and middle
            keys[empty_idx] = keys[middle_idx]
            if items is not None:
                items[empty_idx] = items[middle_idx]
            empty_idx = middle_idx
        # Swap lo_idx and hi_idx as they index out-of-order items
        else:
            _swap(keys, lo_idx, hi_idx)
            if items is not None:
                _swap(items, lo_idx, hi_idx)
            lo_idx += 1
            hi_idx -= 1
    # Place the pivot item in the empty slot
    keys[empty_idx] = pivot_key
    if items is not None:
        items[empty_idx] = pivot_item
    # Recur on partitions (but only if non-empty -- it's possible the
    # pivot was first or last)
    if empty_idx - 1 > start_idx:
        _quick(keys, items, start_idx, empty_idx, pick_pivot)
    if stop_idx > empty_idx + 2:
        _quick(keys, items, empty_idx + 1, stop_idx, pick_pivot)

def quick(items, key=None, pick_pivot=_pivot_median_3):
    # Instantiate items as a list if not indexable
    if not hasattr(items, '__setitem__') or not hasattr(items, '__getitem__'):
        items = list(items)
    # Items are also keys
    if key is None:
        _quick(items, None, 0, len(items), pick_pivot=pick_pivot)
    # Make keys
    else:
        keys = [key(item) for item in items]
        _quick(keys, items, 0, len(items), pick_pivot=pick_pivot)
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
