"""
http://www.geeksforgeeks.org/ugly-numbers/
"""


# function to find ugly numbers
def ugly_numbers_without_set_of_prime(n):
    # create a table to store the n ugly numbers
    ugly = [0 for i in range(n)]
    # first ugly number is 1 by convention
    ugly[0] = 1
    # i2, i3, i5 represents indices of factors 2, 3, 5 respectively all starting at 0
    i2 = i3 = i5 = 0
    # multiple 2
    next_multiple_2 = 2
    # multiple 3
    next_multiple_3 = 3
    # multiple 5
    next_multiple_5 = 5
    # build the table
    for x in range(1, n):
        # update current value with minimum of one of the multiples
        ugly[x] = min(next_multiple_2, next_multiple_3, next_multiple_5)
        # update the multiple that is equal to current ugly number and also the multiple's index
        if ugly[x] == next_multiple_2:
            i2 += 1
            next_multiple_2 = ugly[i2] * 2
        if ugly[x] == next_multiple_3:
            i3 += 1
            next_multiple_3 = ugly[i3] * 3
        if ugly[x] == next_multiple_5:
            i5 += 1
            next_multiple_5 = ugly[i5] * 5
    # return the last element which is the answer
    return ugly[-1]


# find the ugly number
def ugly_numbers_with_set_of_prime(n, s):
    # create a table to store the n ugly numbers
    ugly = [0 for i in range(n)]
    # first ugly number is 1 by convention
    ugly[0] = 1
    # prime number multiple indices
    index = [0 for i in range(len(s))]
    # multiple list
    next_multiple = list(s)
    # build the table
    for x in range(1, n):
        # find the minimum of the multiples and update it
        ugly[x] = min(next_multiple)
        # find the appropriate multiple and update the ugly number
        for i in range(len(next_multiple)):
            if ugly[x] == next_multiple[i]:
                index[i] += 1
                next_multiple[i] = ugly[index[i]] * s[i]
    # return the last element which is the required ugly number
    return ugly[-1]


# driver program to test the above function
print(ugly_numbers_without_set_of_prime(150))
print(ugly_numbers_with_set_of_prime(150, [2, 3, 5]))
