"""
http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
"""


# find the minimum edits (insert or delete or add) between two strings
def count_edit_distance(a, b):
    w = len(a)
    h = len(b)
    t = [[1 for x in range(w + 1)] for y in range(h + 1)]
    t[0][0] = 0
    for i in range(1, w + 1):
        t[0][i] = t[0][i - 1] + 1
    for i in range(1, h + 1):
        t[i][0] = t[i - 1][0] + 1
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if a[j - 1] == b[i - 1]:
                t[i][j] = t[i - 1][j - 1]
            else:
                t[i][j] = min(t[i][j - 1], t[i - 1][j], t[i - 1][j - 1]) + 1
    # print(t)
    return t[h][w]


# driver program to test the above function
print(count_edit_distance("geek", "gesek"))
