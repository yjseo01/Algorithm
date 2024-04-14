#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t, n;
    cin >> t;

    vector<int> vec;

    while (t > 0) {
        t--;
        cin >> n;

        while (n > 0) {
            vec.push_back(n % 2);
            n = n / 2;
        }

        for (int i = 0; i < vec.size(); i++) {
            if (vec[i] == 1)
                cout << i << " ";
        }

        cout << "\n";
        vec.clear();
    }

    return 0;
}