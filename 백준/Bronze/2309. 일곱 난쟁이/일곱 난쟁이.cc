#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    int add = 0;
    int input;
    int arr[9];

    for (int i = 0; i < 9; i++) {
        cin >> input;
        arr[i] = input;
        add += input;
    }

    add = add - 100;

    for (int i = 0; i < 9; i++) {
        for (int j = i + 1; j < 9; j++) {
            if (arr[i] + arr[j] == add) {
                arr[i] = 0;
                arr[j] = 0;
                break;
            }
        }

        if (arr[i] == 0)
            break;
    }

    sort(arr, arr + 9);

    for (int i = 0; i < 9; i++) {
        if (arr[i] != 0)
            cout << arr[i] << "\n";
    }

    return 0;
}
