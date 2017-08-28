"""
http://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
"""

import sys


# find the minimum number of coins required to get the change(n) from the given coin set
def min_coin_change(c, n):
    # creating the table to store minimum coins needed
    t = [sys.maxsize - 1 for i in range(n + 1)]
    # initializing the first element with 0
    t[0] = 0
    # creating another table to store index of which coins used
    l = [-1 for i in range(n + 1)]
    # building the table
    for j in range(len(c)):
        for i in range(1, n + 1):
            # checking if the coin[j] denomination reaches the total i and has a minimum value
            if i >= c[j] and t[i] > t[i - c[j]] + 1:
                # updating the minimum coins required
                t[i] = t[i - c[j]] + 1
                # updating which coin used to get the minimum value
                l[i] = j
    # print the coins used to get the total
    print(coins_used(l, c))
    return t[n] if t[n] != sys.maxsize - 1 else -1


# return a list of minimum coins used to get the total
def coins_used(l, c):
    n = len(l) - 1
    # the coins list
    coins = []
    # start at the last
    i = n
    # loop till i >= 0
    while i >= 0:
        # if l[i] is now -1 then we used the coin in that index
        if l[i] != -1:
            coins.append(c[l[i]])
        # decrement i value by the coin value at l[i]
        i = i - c[l[i]]
    # return the reversed list of the coins to get the order in which we took the coin
    return coins[::-1]


# driver program to test the above function
print(min_coin_change([9, 6, 5, 1], 11))
