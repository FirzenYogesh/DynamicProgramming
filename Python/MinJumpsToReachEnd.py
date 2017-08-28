"""
http://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
"""

import sys


def min_jumps_recursion(a, s, e):
    n = len(a)
    # if we have reached the end number of steps taken is 0
    if s == e:
        return 0
    # if the step value is beyond the size of array
    if a[s] > n:
        return -1
    # if the step value is 0 or less we cannot reach anymore steps
    if a[s] <= 0:
        return -1
    # we traverse through all the points in the array
    i = s + 1
    m = sys.maxsize
    while i <= s + a[s] and i <= e and a[i] < n:
        jump = min_jumps_recursion(a, i, e)
        if jump != -1 and jump + 1 < m:
            m = jump + 1
        i = i + 1
    # we return the minimum value
    return m if m != sys.maxsize else -1


# find the minimum number of jumps to reach the end
def min_jumps(a):
    n = len(a)
    # create a table to store the minimum number of jumps
    t = [sys.maxsize for i in range(n)]
    # create a table to store which steps taken to reach the end
    l = [-1 for i in range(n)]
    # initialize the first index to 0
    t[0] = 0
    # build the table from index i to n and j to i respectively
    for i in range(1, n):
        for j in range(0, i):
            # to check if we can reach the index i and also checking the table value is minimum
            if a[j] + j >= i and t[j] + 1 < t[i]:
                # updating the table when we have a minimum value
                t[i] = t[j] + 1
                # updating the table from where we got the index
                l[i] = j
    return t[n - 1] if t[n - 1] != sys.maxsize else -1


"""driver program to test the above function"""
# using recursion
# [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9] test case
print(min_jumps_recursion([2, 3, 1, 1, 2, 4, 2, 0, 1, 1], 0, 9))
# using dynamic programming
# [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(min_jumps([2, 3, 1, 1, 2, 4, 2, 0, 1, 1]))
