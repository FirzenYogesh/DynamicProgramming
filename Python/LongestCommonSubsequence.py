"""
http://www.geeksforgeeks.org/longest-common-subsequence/
"""


# get the count of longest commom subsequence
def get_longest_common_subsequence(a, b, t):
    r = len(a) + 1
    c = len(b) + 1
    for i in range(1, r):
        for j in range(1, c):
            if a[i - 1] == b[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    return t[r - 1][c - 1]


"""
http://www.geeksforgeeks.org/printing-longest-common-subsequence/
"""


# get the of longest commom subsequence
def print_longest_common_subsequence(a, b, t):
    r = len(a)
    c = len(b)
    count = get_longest_common_subsequence(a, b, t)
    print(count)
    l = [0 for i in range(count + 1)]
    i = r
    j = c
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            l[count - 1] = a[i - 1]
            i -= 1
            j -= 1
            count -= 1
        elif t[i - 1][j] == t[i][j]:
            i -= 1
        else:
            j -= 1
    return l[:-1]


# driver program to test the above functions
s1 = "AGGTAB"
s2 = "GXTXAYB"
arr = [[0 for x in range(len(s2) + 1)] for i in range(len(s1) + 1)]
print(print_longest_common_subsequence(s1, s2, arr))
