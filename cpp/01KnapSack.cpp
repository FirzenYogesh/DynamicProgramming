//
// Created by Yogesh on 30-08-2017.
//

#include <iostream>
#include <algorithm>

using namespace std;

int O1_knapsack(const int values[], const int weights[], const int n, const int weight) {
    int t[n + 1][weight + 1];
    fill(t[0], t[0] + ((n + 1) * (weight + 1)), 0);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= weight; j++) {
            if (j < weights[i - 1])
                t[i][j] = t[i - 1][j];
            else
                t[i][j] = max((values[i - 1] + t[i - 1][j - weights[i - 1]]), t[i - 1][j]);
        }
    }
    return t[n][weight];
}

int main() {
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int w = 50;
    int n = (sizeof(val) / sizeof(val[0]));
    cout << O1_knapsack(val, wt, n, w) << endl;
    return 0;
}
