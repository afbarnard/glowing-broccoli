# Practice problems


# Making change (dynamic programming)
#
# Given denominations x_i and amount n, find the fewest coins that sum
# to n
#
# m[0] = 0
# m[n] = 1 + min(x_i <= n, min[n - x_i])
# d[0] = 0
# d[n] = argmin(x_i <= n, min[n - x_i])
def change(denoms, amount):
    # Prefer large denominations
    denoms = sorted(set(denoms), reverse=True)
    m = [0]
    d = [0]
    for a in range(1, amount + 1):
        min_m = None
        min_d = None
        for d in denoms:
            m_minus_d = m[a - d]
            if min_m is None or m_minus_d < min_m:
                min_m = m_minus_d
                min_d = d
        m.append(1 + min_m)
        d.append(min_d)
    # Convert to actual list of denominations
    chng = []
    a_back = a
    while a_back > 0:
        coin = d[a_back]
        chng.append[coin]
        a_back -= coin
    return chng
