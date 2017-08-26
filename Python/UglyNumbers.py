"""
http://www.geeksforgeeks.org/ugly-numbers/
"""


# function to find ugly numbers
def ugly_numbers(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    next_multiple_2 = 2
    next_multiple_3 = 3
    next_multiple_5 = 5
    for x in range(1, n):
        ugly[x] = min(next_multiple_2, next_multiple_3, next_multiple_5)
        if ugly[x] == next_multiple_2:
            i2 += 1
            next_multiple_2 = ugly[i2] * 2
        if ugly[x] == next_multiple_3:
            i3 += 1
            next_multiple_3 = ugly[i3] * 3
        if ugly[x] == next_multiple_5:
            i5 += 1
            next_multiple_5 = ugly[i5] * 5
    return ugly[-1]


# driver program to test the above function
print(ugly_numbers(150))
