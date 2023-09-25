#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> vec;
    vec.reserve(n + 1);

    vec[0] = 0;
    vec[1] = 1;

    for (int i = 2; i <= n; i++) {
        vec[i] = vec[i - 1] + vec[i - 2];
    }

    cout << vec[n] << "\n";
    return 0;
}
