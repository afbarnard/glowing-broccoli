# Practice problems


# Making change (dynamic programming)
#
# Given denominations x_i and amount n, find the fewest coins that sum
# to n
#
# mins[0] = 0
# mins[n] = 1 + min(x_i <= n, min[n - x_i])
# dens[0] = 0
# dens[n] = argmin(x_i <= n, min[n - x_i])
def change(denoms, amount):
    # Prefer large denominations
    denoms = sorted(set(denoms), reverse=True)
    mins = [0]
    dens = [0]
    for amt in range(1, amount + 1):
        min_mins = None
        min_dens = None
        for den in denoms:
            # Skip denominations larger than the current amount
            if den > amt:
                continue
            m_minus_d = mins[amt - den]
            if min_mins is None or m_minus_d < min_mins:
                min_mins = m_minus_d
                min_dens = den
        mins.append(1 + min_mins)
        dens.append(min_dens)
    # Convert to actual list of denominations
    chng = []
    while amount > 0:
        coin = dens[amount]
        chng.append(coin)
        amount -= coin
    return chng

denoms_us = (1, 5, 10, 25, 50, 100)
denoms_uk = (1, 2, 5, 10, 20, 50, 100, 200)
denoms_euro = denoms_uk # Euros same as pounds
denoms_fib = (1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
denoms_prev2_plus1 = (1, 2, 4, 7, 12, 20, 33, 54, 88)

def print_change(denoms, max_amount=100):
    for amount in range(max_amount + 1):
        print(amount, ': ', change(denoms, amount), sep='')
