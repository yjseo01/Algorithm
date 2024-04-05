#include <iostream>

using namespace std;

int main() {
    int n, cnt, mul;

    while (!(cin >> n).eof()) {
        mul = 1;
        cnt = 1;

        while (mul % n != 0) {
            mul = mul * 10 + 1;
            mul %= n;
            cnt++;
        }

        cout << cnt << "\n";
    }

    return 0;
}
