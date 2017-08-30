//
// Created by Yogesh on 30-08-2017.
//
#include <iostream>

using namespace std;

void show(int array[], int start, int end) {
    cout << "[";
    for (int i = start; i < end; i++) {
        cout << array[i];
        if (i < end - 1)
            cout << " , ";
    }
    cout << "]" << endl;
}

int largest_sum_contiguous_sub_array(int array[]) {
    int n = sizeof(array);
    int max_so_far = array[0];
    int max_ending_here = 0;
    int start = 0, end = 0, s = 0;
    for (int i = 0; i < n; i++) {
        max_ending_here += array[i];
        if (max_ending_here < 0) {
            max_ending_here = 0;
            s = i + 1;
        }
        if (max_so_far < max_ending_here) {
            max_so_far = max_ending_here;
            start = s;
            end = i + 1;
        }
    }
    show(array, start, end);
    return max_so_far;
}

int main() {
    int array[] = {-2, -3, 4, -1, -2, 1, 5, -3};
    cout << largest_sum_contiguous_sub_array(array);
    return 0;
}


