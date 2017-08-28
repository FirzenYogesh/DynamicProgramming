"""
http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
"""


# find the minimum edits (insert or delete or add) between two strings
def count_edit_distance(a, b):
    w = len(a)
    h = len(b)
    # create a table to store the minimum edits required
    t = [[1 for x in range(w + 1)] for y in range(h + 1)]
    # base case (i.e., for two null string edit is 0)
    t[0][0] = 0
    # updating the first row when we have first string as null
    for i in range(1, w + 1):
        t[0][i] = t[0][i - 1] + 1
    # updating the first column when we have second string as null
    for i in range(1, h + 1):
        t[i][0] = t[i - 1][0] + 1
    # building the rest of the table
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            # if we have same value update the current value with the left diagonal value
            if a[j - 1] == b[i - 1]:
                t[i][j] = t[i - 1][j - 1]
            # else we take the minimum of the values(left or top, left diagonal) + 1
            else:
                t[i][j] = min(t[i][j - 1], t[i - 1][j], t[i - 1][j - 1]) + 1
    # return the last value as it has the minimum edits
    return t[h][w]


# driver program to test the above function
print(count_edit_distance("geek", "gesek"))
