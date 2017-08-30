#include <iostream>

using namespace std;

void show(int a[], int n) {
    for (int i = 0; i < n; i++) {
        cout << a[i];
    }
    cout << endl;
}

int main() {
    int a[] = {1, 3, 2, 6, 7, 9, 2, 0};
    return 0;
}