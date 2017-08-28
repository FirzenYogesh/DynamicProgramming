"""
http://www.geeksforgeeks.org/longest-increasing-subsequence/
"""


# find the longest increasing subsequence of a given array
def longest_increasing_subsequence(a):
    n = len(a)
    # if length of the array is zero then we have no sub-sequence
    if n == 0:
        return 0
    # create the table to store the longest sub-sequence
    t = [1 for i in range(n)]
    # build the table
    for i in range(1, n):
        for j in range(0, i):
            # if the ith element is greater than jth we update the table at i with the sum at (j) + 1
            if a[i] > a[j] and t[i] < t[j] + 1:
                t[i] = t[j] + 1
    # return the last element which contains the longest increasing sub-sequence
    return t[n - 1]


# driver program to test the above function
print(longest_increasing_subsequence(list(map(int, "86 177 115 193 135 186 92 49 21 162 27 90 59 163 126 140 26 172 "
                                                   "136 11 168 167 29 182 130 62 123 67 135 129 2 22 58 69 167 193 56 "
                                                   "11 42 29 173 21 119 184 137 198 124 115 170 13 126 91 180 156 73 "
                                                   "62 170 196 81 105 125 84 127 136 105 46 129 113 57 124 95 182 145 "
                                                   "14 167 34 164 43 150 87 8 76 178".split()))))
