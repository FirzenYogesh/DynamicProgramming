"""
http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
"""


# find the number of ways in which we can get the given change for the given set of coins
def coin_change(c, n):
    # creating the table to store the number of ways to get the total
    t = [[1 for i in range(n + 1)] for i in range(len(c) + 1)]
    # if we no coin but we have a total >= 0 we make the first row 0
    for i in range(n + 1):
        t[0][i] = 0
    # building the table
    for i in range(1, len(c) + 1):
        for j in range(1, n + 1):
            # updating the table only if the current total is greater than the current coin denomination is greater
            # or equal
            if j >= c[i - 1]:
                t[i][j] = t[i - 1][j] + t[i][j - c[i - 1]]
            # if not the above case we update with the previous row value
            else:
                t[i][j] = t[i - 1][j]
    return t[len(c)][n]


# driver program to test the above function
print(coin_change([2, 5, 3, 6], 10))
