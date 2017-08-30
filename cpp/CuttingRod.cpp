//
// Created by Yogesh on 30-08-2017.
//
#include <iostream>
#include <algorithm>

using namespace std;

int cutting_rod(const int price[], int length) {
    int t[length + 1];
    fill(t + 0, t + length + 1, 0);
    for (int i = 1; i <= length; i++) {
        for (int j = i; j <= length; j++) {
            t[j] = max(t[j], t[j - i] + price[i - 1]);
        }
    }
    return t[length];
}

int main() {
    int price[] = {1, 4, 5, 5};
    cout << cutting_rod(price, 4);
    return 0;
}

