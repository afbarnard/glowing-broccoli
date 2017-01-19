# Practice implementations of various sorting algorithms

import random


def _swap(items, idx1, idx2):
    swap = items[idx1]
    items[idx1] = items[idx2]
    items[idx2] = swap

def _pivot_first(keys, start_idx, stop_idx):
    return keys[start_idx]

def _pivot_median_3(keys, start_idx, stop_idx):
    # Get the first, middle, and last keys
    key_first = keys[start_idx]
    middle_idx = (start_idx + stop_idx) // 2
    key_middle = keys[middle_idx]
    last_idx = stop_idx - 1
    key_last = keys[last_idx]
    # Find the median
    if key_middle <= key_first <= key_last or key_last <= key_first <= key_middle:
        return key_first
    elif key_first <= key_middle <= key_last or key_last <= key_middle <= key_first:
        return key_middle
    else:
        return key_last

def _pivot_random(keys, start_idx, stop_idx):
    idx = random.randrange(start_idx, stop_idx)
    return keys[idx]

def _quick(keys, items, start_idx, stop_idx, pivot_func=_pivot_first):
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
    pivot_key = pivot_func(keys, start_idx, stop_idx)
    # Partition items based on the pivot.  Items equal to the pivot go
    # in the low partition.
    lo_idx = start_idx
    hi_idx = last_idx
    while lo_idx < hi_idx:
        if keys[lo_idx] <= pivot_key:
            lo_idx += 1
        elif keys[hi_idx] > pivot_key:
            hi_idx -= 1
        else:
            # lo_idx and hi_idx now index out-of-order items.  Swap them.
            _swap(keys, lo_idx, hi_idx)
            if items is not None:
                _swap(items, lo_idx, hi_idx)
            lo_idx += 1
            hi_idx -= 1
    # The pivot is now placed in lo_idx (or before if equal keys)
    # Recur on partitions (but only if non-empty -- it's possible the
    # pivot was first or last)
    if lo_idx - 1 > start_idx:
        _quicksort(keys, items, start_idx, lo_idx - 1)
    if stop_idx > lo_idx + 1:
        _quicksort(keys, items, lo_idx + 1, stop_idx)

def quick(items, key=None, pivot_func=_pivot_median_3):
    # Instantiate items as a list if not indexable
    if not hasattr(items, '__setindex__') or not hasattr(items, '__getindex__'):
        items = list(items)
    # Items are also keys
    if key is None:
        _quicksort(items, None, 0, len(items), pivot_func=pivot_func)
    # Make keys
    else:
        keys = [key(item) for item in items]
        _quicksort(keys, items, 0, len(items), pivot_func=pivot_func)
    return items
