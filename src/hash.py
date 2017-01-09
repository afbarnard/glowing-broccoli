# Hash tables, etc.

from . import tests


def universal_hashing(key, prime=0):
    return key


class LinearGrowthHashTable:
    """Linear growth hash table as used in DBs."""

    def __init__(self, load_factor=0.5, bucket_capacity=2):
        self._load_factor = load_factor
        self._bucket_capacity = bucket_capacity
        self._n_items = 0
        self._key_width = 1
        # List of buckets of items.  There must be at least enough
        # buckets to support the key width.
        self._buckets = [[], []]

    def __len__(self):
        return self._n_items

    def _bucket_index(self, item):
        # Get the hashed key
        key = hash(item)
        #hkey = universal_hashing(key)
        # Mask off lower order bits to find bucket, slighly different than mod?
        bucket_idx = (2 ** self._key_width - 1) & key
        # Strip the highest bit to bring the index into range if necessary
        if bucket_idx >= len(self._buckets):
            bucket_idx -= 2 ** (self._key_width - 1)
        return bucket_idx

    def _lookup(self, item):
        """Return the indices (bucket, item) of the item, or just the
        indices of its bucket (bucket, None) if not found.
        """
        bucket_idx = self._bucket_index(item)
        # Find the item in this bucket
        bucket = self._buckets[bucket_idx]
        for item_idx in range(len(bucket)):
            if bucket[item_idx] == item:
                return (bucket_idx, item_idx)
        return (bucket_idx, None)

    def __contains__(self, item):
        bucket_idx, item_idx = self._lookup(item)
        return item_idx is not None

    def add(self, item):
        bucket_idx, item_idx = self._lookup(item)
        if item_idx is None:
            self._buckets[bucket_idx].append(item)
            self._n_items += 1
        # Grow capacity if needed
        if self._n_items / (len(self._buckets) * self._bucket_capacity) > self._load_factor:
            self._grow()

    def discard(self, item):
        bucket_idx, item_idx = self._lookup(item)
        if item_idx is not None:
            del self._buckets[bucket_idx][item_idx]
            self._n_items -= 1

    def _grow(self):
        """Split the given bucket into the given one and a new one."""
        # Add a bucket "hi"
        hi = []
        hi_idx = len(self._buckets)
        self._buckets.append(hi)
        # Update the key width if needed
        if hi_idx >= 2 ** self._key_width:
            self._key_width += 1
        # Find the corresponding "lo" bucket
        lo = []
        lo_idx = hi_idx - 2 ** (self._key_width - 1)
        # Replace the old lo bucket
        old = self._buckets[lo_idx]
        self._buckets[lo_idx] = lo
        # Split the old items into the new buckets
        for item in old:
            bucket_idx = self._bucket_index(item)
            if bucket_idx == lo_idx:
                lo.append(item)
            elif bucket_idx == hi_idx:
                hi.append(item)
            else:
                ValueError('Hashing Failure: Invalid bucket index: {}'.format(bucket_idx))


class LinearGrowthHashTableTest(tests.SetTest):

    def _new(self, items=()):
        _set = LinearGrowthHashTable()
        for item in items:
            _set.add(item)
        return _set
