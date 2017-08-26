"""
http://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
"""

import sys


# find the minimum number of coins required to get the change(n) from the given coin set
def min_coin_change(c, n):
    t = [sys.maxsize - 1 for i in range(n + 1)]
    t[0] = 0
    l = [-1 for i in range(n + 1)]
    for j in range(len(c)):
        for i in range(1, n + 1):
            if i >= c[j] and t[i] > t[i - c[j]] + 1:
                t[i] = t[i - c[j]] + 1
                l[i] = j
    return t[n] if t[n] != sys.maxsize - 1 else -1


# driver program to test the above function
print(min_coin_change([9, 6, 5, 1], 11))
