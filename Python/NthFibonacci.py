def fib(n, t):
    if t[n] is None:
        if n <= 1:
            t[n] = 1
        else:
            t[n] = fib(n - 2, t) + fib(n - 1, t)
    return t[n]


i = 2
arr = [None for i in range(i + 1)]
print(fib(i, arr))
