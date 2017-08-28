"""
http://www.geeksforgeeks.org/longest-common-subsequence/
"""


# get the count of longest commom subsequence
def get_longest_common_subsequence(a, b):
    r = len(a) + 1
    c = len(b) + 1
    # create table to store the longest common sub-sequence value
    t = [[0 for i in range(c)] for i in range(r)]
    # traverse on both string
    for i in range(1, r):
        for j in range(1, c):
            # if same value update the value as  value of the left diagonal + 1
            if a[i - 1] == b[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            # else update maximum of previous row value or previous column value
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    # we print the longest common sub-sequence
    print(print_longest_common_subsequence(a, b, t))
    # return the last value which has the maximum value
    return t[r - 1][c - 1]


"""
http://www.geeksforgeeks.org/printing-longest-common-subsequence/
"""


# get the of longest commom subsequence
def print_longest_common_subsequence(a, b, t):
    r = len(a)
    c = len(b)
    # we create an empty list to store the sub-sequence
    l = []
    # initialize i with r
    i = r
    # initialize j with c
    j = c
    # loop till either i or j becomes 0
    while i > 0 and j > 0:
        # if same append that value to the list and go to the left diagonal
        if a[i - 1] == b[j - 1]:
            l.append(a[i - 1])
            i -= 1
            j -= 1
        # if value appears in previous row go to that row
        elif t[i - 1][j] == t[i][j]:
            i -= 1
        # if the value is in previous column go to that column
        else:
            j -= 1
    # return the reversed list to get the common sub-sequence in order
    return l[::-1]


# driver program to test the above functions
s1 = "AGGTAB"
s2 = "GXTXAYB"
print(get_longest_common_subsequence(s1, s2))
