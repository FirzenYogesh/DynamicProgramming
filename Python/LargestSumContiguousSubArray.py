"""
http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

Kadane's Algorithm:

max_so_far = array[0]
max_ending_here = 0
for each element i in array
max_ending_here = array[i]
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
    # initialize with first element
    max_so_far = a[0]
    # start index of the contiguous sub-array
    start = 0
    # end index of the contiguous sub-array
    end = 0
    # temporary start index
    s = 0
    # max ending value
    max_end = 0
    # traverse the array
    for i in range(1, n):
        # update max_end with current item
        max_end += a[i]
        # reset max_end if its value is less than 0 and update the temporary start
        if max_end < 0:
            max_end = 0
            s = i + 1
        # if not the above case check the condition and update accordingly
        elif max_so_far < max_end:
            max_so_far = max_end
            start = s
            end = i
    # print the start and the end index of our contiguous array
    print("Start : ", start, " End : ", end)
    # return the largest sum
    return max_so_far


# driver program to test the above function
print("Largest Sum : ", largest_sum_contiguous_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))
