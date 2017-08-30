//
// Created by Yogesh on 30-08-2017.
//
#include <iostream>
#include <algorithm>
#include <list>

void coins_used(const int l[], const int coins[], int total);

using namespace std;


int min_coin_change(const int coins[], int total, int n) {
    int t[total + 1];
    int l[total + 1];
    fill(t + 0, t + (total + 1), INT_MAX - 1);
    fill(l + 0, l + (total + 1), -1);
    t[0] = 0;
    for (int j = 0; j < n; j++) {
        for (int i = 1; i <= total; i++) {
            if (i >= coins[j] && t[i] > t[i - coins[j]] + 1) {
                t[i] = t[i - coins[j]] + 1;
                l[i] = j;
            }
        }
    }
    coins_used(l, coins, total);
    return t[total];
}

void coins_used(const int l[], const int coins[], int total) {
    list<int> used_coins;
    int i = total;
    while (i >= 0 && l[i] != -1) {
        used_coins.push_front(coins[l[i]]);
        i -= coins[l[i]];
    }
    cout << "[";
    while (!used_coins.empty()) {
        cout << used_coins.front();
        used_coins.pop_front();
        if (!used_coins.empty())
            cout << " , ";
    }
    cout << "]" << endl;
}

int main() {
    int coins[] = {9, 6, 5, 1};
    int n = sizeof(coins) / sizeof(coins[0]);
    cout << min_coin_change(coins, 11, n);
}

