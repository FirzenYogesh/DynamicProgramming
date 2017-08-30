"""
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k).

http://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/
"""


# calculate the binomial coefficient of C(n, k) or nCk
def binomial_coefficient(n, r):
    # create a table to store nCr of a number
    a = [[1 for i in range(r + 1)] for i in range(n + 1)]
    # build the table
    for i in range(1, n + 1):
        for j in range(1, r + 1):
            # if j is either 0 or equal to i then we update value as 1
            if j == 0 or j == i:
                a[i][j] = 1
            # if not the case above we update with the sum of left diagonal and the value from previous row
            else:
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    return a[n][r]  # a[n][r] % (mod_value)  if asked to mod the value mod it


# driver function to test the above function
def driver():
    n = 5
    r = 2
    if n >= r:
        print(binomial_coefficient(n, r))
    else:
        print(0)


# calling driver function
driver()
