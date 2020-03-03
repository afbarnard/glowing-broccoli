# 122. Best Time to Buy and Sell Stock II
#
# Say you have an array for which the i-th element is the price of a
# stock on day i.
#
# Design an algorithm to find the maximum profit.  You may complete as
# many buys and sells as you like, but you must hold at most one share
# at a time.


# It seems like this has to be a dynamic programming problem, but it's
# marked as easy.  So I'm probably missing some sort of greedy strategy.
# Investigate!

#  [ 1, 10,  2, 12,  3, 14,  4, 16]
#    0   1   2   3   4   5   6   7
# 0      9   9  19  19  30  30  42
# 1          0  10  10  21  21  33
# 2             10  10  21  21  33
# 3                  0  11  11  23
# 4                     11  11  23
# 5                          0  12
# 6                             12

#  [ 1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
#    0  1  2  3  4  5  6  7  8  9
# 0     1  3  3  6  8  8 10 15 15
# 1        2  2  5  7  7  9 14 14
# 2           0  3  5  5  7 12 12
# 3              3  5  5  7 12 12
# 4                 2  2  4  9  9
# 5                    0  2  7  7
# 6                       2  7  7
# 7                          5  5
# 8                             0

# Well, it turns out that the following properties of sequences of
# numbers can be taken advantage of to create an optimal method that
# does not require dynamic programming.
#
# * A sequence of numbers is composed of consecutive subsequences that
#   are either monotonically increasing or monotonically decreasing.
#   The subsequences alternate between increasing and decreasing when
#   considered to share end points.
# * Extend increasing subsequences as far as possible in each direction
#   maximizes the difference: Given a_i <= ... <= a_j <= ... <= a_k <=
#   ... <= a_n, (a_n - a_i) >= (a_k - a_j) because a_n >= a_k and a_j >=
#   a_i.
# * The difference of a decreasing sequence is <= 0, so it is best to
#   not buy or sell.
# * Choosing from a decreasing sequence following an increasing sequence
#   cannot increase the difference of the increasing sequence: Given a_i
#   <= ... <= a_j >= ... >= a_k, (a_j - a_i) >= (a_k - a_i).
# * Similarly, choosing a starting point in a decreasing sequence
#   followed by an increasing sequence cannot increase the difference of
#   the increasing sequence: Given a_i >= ... >= a_j <= ... <= a_k, (a_k
#   - a_j) >= (a_k - a_i).
# * In an increasing, decreasing, increasing scenario, it is always best
#   to treat both increasing sequences separately.  Given a_i <= ... <=
#   a_j >= ... >= a_k <= ... <= a_n, (a_j - a_i) + (a_n - a_k) >= (a_n -
#   a_i) because a_j >= a_k.
#
# Together with inducution, these properties cover all possible
# sequences of numbers and show that the maximum differences are
# obtained from the maximal increasing subsequences which can be found
# with a linear scan.


# In a strategy, a buy is -1, a sell is 1, and a hold is 0.
# Thus, the profit is the dot product of the strategy vector
# with the prices vector.

def gen_strategies(length: int):
    strategy = [0] * length
    yield strategy
    idx = 0
    while idx < length:
        # Increment to the next strategy
        if strategy[idx] == 0:
            strategy[idx] = -1
            idx = 0
            yield strategy
        elif strategy[idx] == -1:
            strategy[idx] = 1
            idx = 0
            yield strategy
        else:
            assert strategy[idx] == 1
            strategy[idx] = 0
            idx += 1

def is_valid_strategy(strategy):
    """A valid strategy comes in pairs of buys and sells."""
    cumsum = 0
    for num in strategy:
        cumsum += num
        if cumsum > 0:
            return False
        elif cumsum < -1:
            return False
    return True

def profit(prices, strategy):
    return sum(prices[i] * strategy[i] for i in range(len(prices)))

def max_profit_dynprg(prices, idx_beg=None, idx_end=None, table=None):
    if idx_beg is None:
        idx_beg = 0
    if idx_end is None:
        idx_end = len(prices) - 1
    if table is None:
        table = {}
    # Ensure sensical arguments.  If not, return 0.
    if idx_beg >= idx_end or idx_beg < 0 or idx_end >= len(prices):
        return 0
    # Look up the existing maximum profit for this range of indices
    max_prft = table.get((idx_beg, idx_end), None)
    # Compute the max profit if it hasn't been computed before
    if max_prft is None:
        prfts = [
            # No buys, no sells
            0,
            # Buy at beginning, sell at end
            prices[idx_end] - prices[idx_beg],
        ]
        length = idx_end - idx_beg + 1
        if length >= 3:
            # Single intervals of length 1 less
            prfts.append(max_profit_dynprg(
                prices, idx_beg, idx_end - 1, table))
            prfts.append(max_profit_dynprg(
                prices, idx_beg + 1, idx_end, table))
        if length >= 4:
            # Single interval of length 2 less
            prfts.append(max_profit_dynprg(
                prices, idx_beg + 1, idx_end - 1, table))
            # All pairs of intervals
            for idx_mid in range(idx_beg + 1, idx_end - 1):
                prfts.append(
                    max_profit_dynprg(prices, idx_beg, idx_mid, table)
                    +
                    max_profit_dynprg(prices, idx_mid + 1, idx_end, table)
                )
        max_prft = max(prfts)
        table[idx_beg, idx_end] = max_prft
        #print(f'{idx_beg}-{idx_end}: {max_prft}')
    return max_prft

def max_profit_dynprg_nonrec(prices):
    if len(prices) < 2:
        return 0
    table = {}
    for length in range(2, len(prices) + 1):
        #print(f'length: {length}')
        for idx_beg in range(0, len(prices) - length + 1):
            idx_end = idx_beg + length - 1
            prfts = [
                # No buys, no sells
                0,
                # Buy at beginning, sell at end
                prices[idx_end] - prices[idx_beg],
            ]
            if length >= 3:
                # Single intervals of length 1 less
                prfts.append(table[idx_beg, idx_end - 1])
                prfts.append(table[idx_beg + 1, idx_end])
            if length >= 4:
                # All pairs of adjoining, smaller intervals
                for idx_mid in range(idx_beg + 1, idx_end - 1):
                    prfts.append(table[idx_beg, idx_mid] +
                                 table[idx_mid + 1, idx_end])
            max_prft = max(prfts)
            table[idx_beg, idx_end] = max_prft
            #print(f'{idx_beg}-{idx_end}: {max_prft}')
    return table[0, len(prices) - 1]

class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        max_profit = 0
        for strategy in gen_strategies(len(prices)):
            if not is_valid_strategy(strategy):
                continue
            # Compute the profit of this strategy
            prft = profit(prices, strategy)
            if max_profit is None or prft > max_profit:
                max_profit = prft
        return max_profit

    def maxProfit_2(self, prices: List[int]) -> int:
        prices_length = len(prices)
        if prices_length < 2:
            return 0
        max_profit = 0
        for idx1 in range(prices_length - 1):
            price_buy = prices[idx1]
            for idx2 in range(idx1 + 1, prices_length):
                price_sell = prices[idx2]
                if price_sell <= price_buy:
                    continue
                prft = price_sell - price_buy
                if prices_length - idx2 > 2:
                    prft += self.maxProfit_2(prices[idx2 + 1:])
                if prft > max_profit:
                    max_profit = prft
        return max_profit

    def maxProfit_3(self, prices: List[int]) -> int:
        return max_profit_dynprg(prices)

    def maxProfit_4(self, prices: List[int]) -> int:
        return max_profit_dynprg_nonrec(prices)

    def maxProfit_5(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        prft = 0
        prices_iter = iter(prices)
        prev_price = next(prices_iter)
        for curr_price in prices_iter:
            if curr_price > prev_price:
                prft += curr_price - prev_price
            prev_price = curr_price
        return prft

    maxProfit = maxProfit_5
