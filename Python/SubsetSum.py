"""
http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/
"""


def subset_sum(array, s):
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


print(subset_sum(sorted([3, 34, 4, 12, 5, 2]), 9))
