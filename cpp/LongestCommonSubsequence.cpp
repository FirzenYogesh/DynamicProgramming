//
// Created by Yogesh on 30-08-2017.
//

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int longest_common_sub_sequence(char * /*s1*/, char * /*s2*/);

void print_longest_common_sub_sequence(char *, char *, int[][]);

int longest_common_sub_sequence(char *s1, char *s2) {
    size_t n = strlen(s1) + 1;
    size_t m = strlen(s2) + 1;
    int t[n][m];
    fill(t[0], t[0] + (n * m), 0);
    for (size_t i = 1; i < n; i++) {
        t[0][i] = t[0][i - 1] + 1;
    }
    for (size_t i = 1; i < m; i++) {
        t[i][0] = t[i - 1][0] + 1;
    }
    for (size_t i = 1; i < n; i++) {
        for (size_t j = 1; j < m; j++) {
            if (s1[i - 1] == s2[j - 1])
                t[i][j] = t[i - 1][j - 1] + 1;
            else
                t[i][j] = max(t[i][j - 1], t[i - 1][j]);
        }
    }
    print_longest_common_sub_sequence(s1, s2, t);
    return t[n][m];
}

void print_longest_common_sub_sequence(char *s1, char *s2, int t[][]) {

}