"""
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k).

http://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/
"""


# calculate the binomial coefficient of C(n, k) or nCk
def binomial_coefficient(n, k):
    a = [[1 for c in range(k + 1)] for r in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    return a[n][k]  # if asked to mod the value mod it


# driver function to test the above function
def driver():
    n = 5
    k = 2
    if n >= k:
        print(binomial_coefficient(n, k))
    else:
        print(0)


# calling driver function
driver()
