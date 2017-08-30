//
// Created by Yogesh on 30-08-2017.
//
#include <iostream>
#include <algorithm>

using namespace std;

int number_of_ways(const int coins[], int total, int n) {
    int t[n + 1][total + 1];
    fill(t[0], t[0] + ((n + 1) * (total + 1)), 1);
    for (int i = 0; i < total + 1; i++) {
        t[0][i] = 0;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= total; j++) {
            if (j < coins[i - 1])
                t[i][j] = t[i - 1][j];
            else
                t[i][j] = t[i - 1][j] + t[i][j - coins[i - 1]];
        }
    }
    return t[n][total];
}

int main() {
    int coins[] = {2, 5, 3, 6};
    int n = sizeof(coins) / sizeof(coins[0]);
    cout << number_of_ways(coins, 10, n);
    return 0;
}
