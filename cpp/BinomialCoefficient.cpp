//
// Created by Yogesh on 30-08-2017.
//
#include <iostream>
#include <algorithm>

using namespace std;

long long binomial_coefficient(int n, int r) {
    if (n < r)
        return 0;
    long long t[n + 1][r + 1];
    fill(t[0], t[0] + ((n + 1) * (r + 1)), 1);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= r; j++) {
            if (i == j || j == 0)
                t[i][j] = 1;
            else
                t[i][j] = t[i - 1][j - 1] + t[i - 1][j];
        }
    }
    return t[n][r];
}

int main() {
    cout << binomial_coefficient(5, 2);
    return 0;
}
