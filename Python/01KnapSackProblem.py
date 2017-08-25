"""
http://www.geeksforgeeks.org/knapsack-problem/
"""


def knapsack_01(val, wt, n, w):
    t = [[1 for c in range(w + 1)] for r in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif j < wt[i - 1]:
                t[i][j] = t[i - 1][j]
            else:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
    return t[n][w]


# Driver function to test the above function
def driver():
    val = [60, 100, 120]
    wt = [10, 20, 30]
    w = 50
    n = len(val)
    print(knapsack_01(val, wt, n, w))


driver()
