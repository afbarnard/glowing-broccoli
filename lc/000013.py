# 13. Roman to Integer
#
# Roman numerals are represented by seven different symbols: I, V, X, L,
# C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two ones added
# together. 12 is written as XII, which is simply X + II. The number 27
# is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to
# right. However, the numeral for four is not IIII. Instead, the number
# four is written as IV. Because the one is before the five we subtract
# it making four. The same principle applies to the number nine, which
# is written as IX. There are six instances where subtraction is used:
#
# * I can be placed before V (5) and X (10) to make 4 and 9.
# * X can be placed before L (50) and C (100) to make 40 and 90.
# * C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer.


# The recognized roman numerals and their values
numeral2decimal = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def roman2decimal(roman_number: str,
                  numeral2decimal: dict[str, int]=numeral2decimal) -> int:
    """
    Convert the given string of Roman numerals (a Roman number) into
    a decimal number.

    Note this is not a general implementation as the Roman number can
    have at most 1 subtractive numeral in a row.  For example, 8 must be
    spelled VIII not IIX (even though the latter would be shorter).
    """
    decimal = 0
    prev = None
    for numeral in roman_number:
        value = numeral2decimal.get(numeral)
        if value is None:
            raise ValueError(f"Unrecognized Roman numeral: '{numeral}' (in '{roman_number}')")
        # Just save this value in case the next numeral is larger
        if prev is None:
            prev = value
        # If the previous numeral is smaller than the current numeral,
        # subtract the previous from the current and add that total to
        # the final number
        elif prev < value:
            decimal += value - prev
            prev = None
        # If the previous numeral is larger than the current numeral,
        # add it to the final number and save the current for the next
        # round
        else:
            decimal += prev
            prev = value
    # Handle any leftover numeral (which has to be additive)
    if prev is not None:
        decimal += prev
    return decimal

# Interface to LeetCode
class Solution:
    def romanToInt(self, s: str) -> int:
        return roman2decimal(s)
