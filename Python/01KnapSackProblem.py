"""
http://www.geeksforgeeks.org/knapsack-problem/
"""


# returns the maximum possible value for the given total weight
def knapsack_01(val, wt, n, w):
    # create a table to store the maximum possible value
    t = [[0 for c in range(w + 1)] for r in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            # if the current weight is less than the ith weight we take previous row value
            if j < wt[i - 1]:
                t[i][j] = t[i - 1][j]
            # else we take the max value of previous row and sum(ith value and t[i-1][j-weight[i-1]]
            else:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
    # return the maximum value which is at the last
    return t[n][w]


# Driver function to test the above function
def driver():
    val = [60, 100, 120]
    wt = [10, 20, 30]
    w = 50
    n = len(val)
    print(knapsack_01(val, wt, n, w))


driver()
