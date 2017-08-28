"""
http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/
"""


# function to find the minimum cost path
def min_cost_path(a, r, c):
    # create a table to find the min cost path
    t = [[0 for x in range(c)] for x in range(r)]
    # first value is the first value of the matrix
    t[0][0] = a[0][0]
    # update the first row path cost
    for i in range(1, r):
        t[i][0] = t[i - 1][0] + a[i][0]
    # update the second row path cost
    for i in range(1, c):
        t[0][i] = t[0][i - 1] + a[0][i]
    # build the remaining table
    for row in range(1, r):
        for col in range(1, c):
            # cost to reach current element is minimum of left, top and left diagonal values
            t[row][col] = a[row][col] + min(t[row - 1][col - 1], t[row - 1][col], t[row][col - 1])
    # return the last element as it has the minimum cost
    return t[r - 1][c - 1]


# driver program to test the above function
print(min_cost_path([[1, 2, 3],
                     [4, 8, 2],
                     [1, 5, 3]], 3, 3))
