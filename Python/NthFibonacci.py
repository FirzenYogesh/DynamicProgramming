"""
Fibonacci using Dynamic Programming
"""


# find the nth fibonacci item
def fib(n, t):
    # only update if the value at n is None/ null
    if t[n] is None:
        # base case
        if n <= 1:
            t[n] = 1
        # update by finding the value
        else:
            t[n] = fib(n - 2, t) + fib(n - 1, t)
    # return the nth element
    return t[n]


# driver program to test the above function
i = 8
arr = [None for i in range(i + 1)]
print(fib(i, arr))
