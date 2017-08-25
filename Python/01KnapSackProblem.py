"""
http://www.geeksforgeeks.org/knapsack-problem/
"""


def knapsack_01(v, w, n, tot):
    t = [[1 for c in range(tot + 1)] for r in range(n + 1)]
    for i in range(n + 1):
        for j in range(tot + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif j < w[i - 1]:
                t[i][j] = t[i - 1][j]
            else:
                t[i][j] = max(v[i - 1] + t[i][j - w[i - 1]], t[i - 1][j])
    return t[n][tot]


# Driver function to test the above function
def driver():
    val = [60, 100, 120]
    wt = [10, 20, 30]
    w = 50
    n = len(val)
    print(knapsack_01(w, wt, val, n))


driver()
