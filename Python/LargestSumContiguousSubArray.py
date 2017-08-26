"""
http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

Kadane's Algorithm:

max_so_far = array[0]
max_ending_here = 0
for each element i in array
check
1)if max_ending_here < 0
    max_ending_here = 0
2)if max_so_far < max_ending_here
    max_so_far = max_ending_here
return max_so_far

"""


# find the largest sum of contiguous subarray using Kadane's Algorithm
def largest_sum_contiguous_subarray(a):
    n = len(a)
    max_sofar = a[0]
    start = 0
    end = 0
    s = 0
    max_end = 0
    for i in range(1, n):
        max_end += a[i]
        if max_end < 0:
            max_end = 0
            s = i + 1
        elif max_sofar < max_end:
            max_sofar = max_end
            start = s
            end = i
    print("Start : ", start, " End : ", end)
    return max_sofar


# driver program to test the above function
print("Largest Sum : ", largest_sum_contiguous_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))
