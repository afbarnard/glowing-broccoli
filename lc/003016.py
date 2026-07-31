# 3016. Minimum Number of Pushes to Type Word II
#
# You are given a string `word` containing lowercase English letters.
#
# Telephone keypads have keys mapped with *distinct* collections of
# lowercase English letters, which can be used to form words by pushing
# them.  For example, the key `2` is mapped with `["a","b","c"]`, we
# need to push the key one time to type `"a"`, two times to type `"b"`,
# and three times to type `"c"`.
#
# It is allowed to remap the keys numbered `2` to `9` to *distinct*
# collections of letters.  The keys can be remapped to *any* amount of
# letters, but each letter *must* be mapped to *exactly* one key.  You
# need to find the *minimum* number of times the keys will be pushed to
# type the string `word`.
#
# Return the *minimum* number of pushes needed to type `word` after
# remapping the keys.
#
# An example mapping of letters to keys on a telephone keypad is given
# below.  Note that `1`, `*`, `#`, and `0` do *not* map to any letters.
#
# •-------------------------•
# | 1      | 2 abc | 3 def  |
# | ------ | ----- | ------ |
# | 4 ghi  | 5 jkl | 6 mno  |
# | ------ | ----- | ------ |
# | 7 pqrs | 8 tuv | 9 wyxz |
# | ------ | ----- | ------ |
# | *      | 0     | #      |
# •-------------------------•

# Ok, so this is basically a Huffman coding problem where the letter
# frequency gets organized into trees, but there are 8 roots and each
# tree is linear (single child, non-branching).
#
# * Use a Counter to collect letter frequencies.
# * Round-robin assign letters to telephone key numbers by decreasing
#   frequency.  Accumulate letters in an array of lists.  Keep a mapping
#   of letters to numbers.  I'm assuming that assigning the shortest
#   codes to the most frequent symbols in a greedy manner will minimize
#   the total code length.
# * Go through the string a final time to total up key presses.


import collections
import string


def count_freqs(items) -> dict[str, int]:
    """
    Count the frequencies of the given items.  Return a mapping of
    items to counts (a Counter).
    """
    return collections.Counter(items)

def ensure_all_symbols(counter, all_symbols) -> dict[str, int]:
    """Add the given symbols to the given Counter with a count of 0."""
    # It would be equivalent to count each symbol an extra time, but
    # let's have the counter keep the actual frequencies
    for symbol in all_symbols:
        counter[symbol] += 0
    return counter

def build_huff_tree(counter) -> list[list[str]]:
    """
    Build the frequency encoding data structure (which is a
    degenerate Huffman tree if it's one at all).
    """
    # The "Huffman tree" has a root for each numerical telephone key,
    # and the children of each root are the symbols assigned to that
    # key.  Keep the roots in a list so that the list index is the
    # numerical telephone key.  Each item in the outer list is a list
    # containing the symbols accessed by pressing that key.  The inner
    # list represents the "linear tree" under a given root.
    huff_tree = [list() for _ in range(10)]
    # The key can only be 2-9
    key = 2
    for (symbol, freq) in counter.most_common():
        huff_tree[key].append(symbol)
        # Increment key, but keep it in •(2,9)•
        key += 1
        if key % 10 == 0:
            key = 2
    return huff_tree

def build_symbol2key(huff_tree) -> dict[str, int]:
    symbol2key = {}
    # The key is the index in the list
    for (key, symbol_chain) in enumerate(huff_tree):
        for symbol in symbol_chain:
            # ENH could check for unique symbols here
            symbol2key[symbol] = key
    return symbol2key

def presses(symbol, symbol2key, huff_tree) -> tuple[int, int]:
    """
    Return the tuple (number to press, how many times to press it)
    for the given symbol.
    """
    key = symbol2key.get(symbol)
    if key is None:
        raise ValueError(f"Unrecognized symbol: '{symbol}'")
    symbol_chain = huff_tree[key]
    try:
        n_presses = symbol_chain.index(symbol)
    except ValueError as e:
        raise ValueError(f"Symbol not found in chain: '{symbol}'.  (Inconsistent encoding data structures.)") from e
    # Convert index to number
    return (key, n_presses + 1)

def total_n_presses(symbols, symbol2key, huff_tree) -> int:
    tot_n_presses = 0
    for symbol in symbols:
        (key, n_presses) = presses(symbol, symbol2key, huff_tree)
        tot_n_presses += n_presses
    return tot_n_presses

def n_presses_to_encode(word: str) -> int:
    counter = count_freqs(word)
    counter = ensure_all_symbols(counter, string.ascii_lowercase)
    huff_tree = build_huff_tree(counter)
    symbol2key = build_symbol2key(huff_tree)
    return total_n_presses(word, symbol2key, huff_tree)


# Interface for LeetCode
class Solution:
    def minimumPushes(self, word: str) -> int:
        return n_presses_to_encode(word)
