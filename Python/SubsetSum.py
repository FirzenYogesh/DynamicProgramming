"""
http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/
"""

"""def is_subset_sum(array, s):
    n = len(array)
    for i in range(1, n):
        t_sum1 = 0
        for j in range(i):
            t_sum2 = array[j] + array[i]
            if t_sum2 == s:
                return True
            t_sum1 += array[j]
        t_sum1 += array[i]
        if t_sum1 == s:
            return True
    return False
"""


# returns true if the set a has a subset whose sum is the given sum else false executes in O(sum*n)
def is_subset_sum(a, s):
    n = len(a)
    # creating the dp table
    t = [[False for i in range(s + 1)] for i in range(n + 1)]
    # if sum is 0 then the answer is true
    for i in range(n + 1):
        t[i][0] = True
    # if sum is not 0 but we have non empty set then answer is false
    for i in range(s + 1):
        t[0][i] = False
    # dp table filling based on the set and sum
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            t[i][j] = t[i - 1][j]
            if j >= a[i - 1]:
                t[i][j] = t[i][j] or t[i - 1][j - a[i - 1]]
    return t[n][s]


"""Driver program to test the above function"""
print(is_subset_sum([3, 34, 4, 12, 5, 2], 9))
