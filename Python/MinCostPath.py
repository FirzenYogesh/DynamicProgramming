"""
http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/
"""


# function to find the minimum cost path
def min_cost_path(a, r, c):
    t = [[0 for x in range(c)] for x in range(r)]
    t[0][0] = a[0][0]
    for i in range(1, r):
        t[i][0] = t[i - 1][0] + a[i][0]
    for i in range(1, c):
        t[0][i] = t[0][i - 1] + a[0][i]
    for row in range(1, r):
        for col in range(1, c):
            t[row][col] = a[row][col] + min(t[row - 1][col - 1], t[row - 1][col], t[row][col - 1])
    return t[r - 1][c - 1]


# driver program to test the above function
print(min_cost_path([[1, 2, 3],
                     [4, 8, 2],
                     [1, 5, 3]], 3, 3))
