# Heaps and priority queues


class Heap:

    def __init__(self):
        self._n_items = 0
        self._items = []

    def __len__(self):
        return self._n_items

    def __contains__(self, item):
        return item in self._items[:self._n_items]

    def _parent_idx(self, idx):
        # 1-based: idx // 2
        return (idx + 1) // 2 - 1

    def _left_idx(self, idx):
        # 1-based: 2 * idx
        return 2 * (idx + 1) - 1

    def _right_idx(self, idx):
        # 1-based: 2 * idx + 1
        return 2 * (idx + 1)

    def _move_up(self, idx):
        # Move this value up until it is less than its parent
        # Base case
        if idx == 0:
            return
        parent_idx = self._parent_idx(idx)
        max_val = self._items[idx]
        if self._items[parent_idx] < max_val:
            # Swap values and continue moving up
            self._items[idx] = self._items[parent_idx]
            self._items[parent_idx] = max_val
            self._move_up(parent_idx)

    def _move_down(self, idx):
        # Move this value down until the heap property is satisfied
        # (parent greater than or equal to both children)
        left_idx = self._left_idx(idx)
        right_idx = self._right_idx(idx)
        # Find the max among this node and its children
        max_val = self._items[idx]
        max_idx = idx
        if left_idx < self._n_items and self._items[left_idx] > max_val:
            max_val = self._items[left_idx]
            max_idx = left_idx
        if right_idx < self._n_items and self._items[right_idx] > max_val:
            max_val = self._items[right_idx]
            max_idx = right_idx
        # Base condition: heap condition satisfied
        if max_idx == idx:
            return
        # Otherwise exchange this value with the maximum and recur on
        # that child
        else:
            self._items[max_idx] = self._items[idx]
            self._items[idx] = max_val
            self._move_down(max_idx)

    def _update(self, idx):
        # Move up or down depending on value
        # Find the maximum value among this node and its children
        max_val = self._items[idx]
        max_idx = idx
        left_idx = self._left_idx(idx)
        right_idx = self._right_idx(idx)
        if left_idx < self._n_items and self._items[left_idx] > max_val:
            max_val = self._items[left_idx]
            max_idx = left_idx
        if right_idx < self._n_items and self._items[right_idx] > max_val:
            max_val = self._items[right_idx]
            max_idx = right_idx
        # If this node is the maximum, move up
        if max_idx == idx:
            self._move_up(idx)
        # Otherwise, move down
        else:
            self._move_down(idx)

    def _heapify(self):
        # 1-based: self._n_items // 2
        start = self._n_items // 2 - 1
        for idx in range(start, -1, -1):
            self._move_down(idx)

    def max(self):
        if self._n_items > 0:
            return self._items[0]
        else:
            return None

    def pop(self):
        max_val = self._items[0]
        # Fill the empty spot with the last value and move it down
        self._n_items -= 1
        if 0 < self._n_items:
            self._items[0] = self._items[self._n_items]
            self._move_down(0)
        return max_val

    def add(self, item):
        if self._n_items < len(self._items):
            self._items[self._n_items] = item
        else:
            self._items.append(item)
        self._n_items += 1
        self._move_up(self._n_items - 1)

    def extend(self, items):
        items = list(items)
        self._items[:self._n_items].extend(items) # TODO returns number of items?
        self._n_items += len(items)
        self._heapify()

    def discard(self, item):
        idx = self._items[:self._n_items].index_of(item)
        if idx < 0:
            return
        # Replace this item with the last item and adjust it up or down
        self._n_items -= 1
        if idx < self._n_items:
            self._items[idx] = self._items[self._n_items]
            self._update(idx)

    def update(self, old, new):
        idx = self._items[:self._n_items].index_of(old)
        if idx < 0:
            return
        self._items[idx] = new
        self._update(idx)
