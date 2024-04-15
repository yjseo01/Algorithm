#include <iostream>

using namespace std;

int main(void) {
    int n = 0, max = 0;
    int a, b;
    for (int i = 0; i < 10; i++) {
        cin >> a;
        cin >> b;

        n = n - a + b;

        if (n > max)
            max = n;
    }

    cout << max << "\n";

    return 0;
}
