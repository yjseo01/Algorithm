#include <iostream>

using namespace std;

int main(void) {
    int x;
    cin >> x;

    long long res = 0;
    for (int i = 1; i <= x; i++)
        res += (x / i) * i;

    cout << res << "\n";

    return 0;
}