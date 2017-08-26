"""
http://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/
"""

import sys


def cutting_rod(price, n):
    t = [[0 for i in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j >= i:
                t[i][j] = max((t[i][j - i] + price[i - 1]), t[i - 1][j], t[i][j - 1], (t[i - 1][j - i] + price[i - 1]))
            else:
                t[i][j] = t[i - 1][j]
    return t[n][n]


def cutting_rod1(price, n):
    t = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            t[j] = max(t[j], t[j - i] + price[i - 1])
    return t[n]


print(cutting_rod([1, 4, 5, 5], 4))
