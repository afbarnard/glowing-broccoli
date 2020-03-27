# 28. Implement `strstr()`.
#
# Return the index of the first occurrence of needle in haystack, or -1
# if needle is not part of haystack.  If `needle` is empty, return 0
# (consistent with `strstr` in C).


# My original, basic solution exceeded the time limit, so I had to
# implement some more complicated solutions.


def strstr_basic(haystack, needle):
    hay_len = len(haystack)
    ndl_len = len(needle)
    if ndl_len == 0:
        return 0
    hay_idx = 0
    while hay_idx <= hay_len - ndl_len:
        ndl_idx = 0
        while (ndl_idx < ndl_len and
               haystack[hay_idx + ndl_idx] == needle[ndl_idx]):
            ndl_idx += 1
        if ndl_idx == ndl_len:
            return hay_idx
        hay_idx += 1
    return -1

def strstr_fingerprint(haystack, needle):
    hay_len = len(haystack)
    ndl_len = len(needle)
    # Exit early if needle is empty or larger than haystack
    if ndl_len == 0:
        return 0
    elif ndl_len > hay_len:
        return -1
    # Analyze the needle to make it easier to search for
    char_idxs = {}
    for idx, c in enumerate(needle):
        idxs = char_idxs.get(c)
        if idxs is None:
            char_idxs[c] = [idx]
        else:
            idxs.append(idx)
    # Rarest characters with latest first occurrences
    rarest = sorted(char_idxs.items(),
                    key=lambda kv: (len(kv[1]), -kv[1][0], kv[0]))
    fgrprt_chars = ''.join(k * len(v) for k, v in rarest)
    fgrprt_idxs = [i for k, v in rarest for i in v]
    # Deallocate
    char_idxs = None
    # Start checking the haystack from the beginning
    hay_idx = 0
    ndl0 = needle[0]
    while hay_idx <= hay_len - ndl_len:
        # Can the current character be the start of a match?
        if haystack[hay_idx] == ndl0:
            # Check the haystack for the fingerprint
            idx = 0
            while (idx < ndl_len and
                   (haystack[hay_idx + fgrprt_idxs[idx]]
                    == fgrprt_chars[idx])):
                idx += 1
            if idx == ndl_len:
                return hay_idx
        # Increment
        hay_idx += 1
    return -1

def strstr_shell(haystack, needle):
    hay_len = len(haystack)
    ndl_len = len(needle)
    # Exit early if needle is empty or larger than haystack
    if ndl_len == 0:
        return 0
    elif ndl_len > hay_len:
        return -1
    # If the initial character of needle repeats in needle, then one can
    # skip forward on a partial match
    ndl0 = needle[0]
    skip = needle.find(ndl0, 1)
    if skip == -1:
        skip = ndl_len
    # Start checking the haystack from the beginning
    hay_idx = 0
    while hay_idx <= hay_len - ndl_len:
        idx1 = 0
        idx2 = ndl_len - 1
        while (idx1 <= idx2 and
               haystack[hay_idx + idx1] == needle[idx1] and
               haystack[hay_idx + idx2] == needle[idx2]):
            idx1 += 1
            idx2 -= 1
        if idx1 > idx2:
            return hay_idx
        hay_idx += min(idx1, skip) if idx1 > 0 else 1
    return -1


class Solution:

    def strStr1(self, haystack: str, needle: str) -> int:
        return strstr_basic(haystack, needle)

    def strStr2(self, haystack: str, needle: str) -> int:
        return strstr_fingerprint(haystack, needle)

    def strStr3(self, haystack: str, needle: str) -> int:
        return strstr_shell(haystack, needle)

    strStr = strStr1
