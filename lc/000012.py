# 12. Integer to Roman
#
# Seven different symbols represent Roman numerals with the following values:
# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
#
# Roman numerals are formed by appending the conversions of decimal
# place values from highest to lowest. Converting a decimal place value
# into a Roman numeral has the following rules:
#
# * If the value does not start with 4 or 9, select the symbol of the
#   maximal value that can be subtracted from the input, append that
#   symbol to the result, subtract its value, and convert the remainder
#   to a Roman numeral.
# * If the value starts with 4 or 9 use the subtractive form
#   representing one symbol subtracted from the following symbol, for
#   example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10
#   (X): IX. Only the following subtractive forms are used: 4 (IV), 9
#   (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# * Only powers of 10 (I, X, C, M) can be appended consecutively at most
#   3 times to represent multiples of 10. You cannot append 5 (V), 50
#   (L), or 500 (D) multiple times. If you need to append a symbol 4
#   times use the subtractive form.
#
# Given an integer, convert it to a Roman numeral.


import math


decimal2numeral = {
    1   : 'I',
    5   : 'V',
    10  : 'X',
    50  : 'L',
    100 : 'C',
    500 : 'D',
    1000: 'M',
}
numeral_values_desc = sorted(decimal2numeral.keys(), reverse=True)

subtractive_forms = {
    # (digit, 10**x): Roman numeral
    (4, 0): 'IV', #   4
    (4, 1): 'XL', #  40
    (4, 2): 'CD', # 400
    (9, 0): 'IX', #   9
    (9, 1): 'XC', #  90
    (9, 2): 'CM', # 900
}

def decimal2roman(number: int) -> str:
    numerals = []
    numeral_val_idx = 0
    numeral_value = numeral_values_desc[numeral_val_idx]
    while number > 0:
        n_places = math.floor(math.log10(number))
        leading_digit = number // 10**n_places
        if number < 4000 and leading_digit in (4, 9):
            numeral = subtractive_forms[leading_digit, n_places]
            numerals.append(numeral)
            number -= leading_digit * 10**n_places
        elif numeral_value <= number:
            numerals.append(decimal2numeral[numeral_value])
            number -= numeral_value
        else:
            numeral_val_idx += 1
            numeral_value = numeral_values_desc[numeral_val_idx]
    return ''.join(numerals)


# Interface to LeetCode
class Solution:
    def intToRoman(self, num: int) -> str:
        return decimal2roman(num)
