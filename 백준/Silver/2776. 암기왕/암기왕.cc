#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t-- > 0) {
        int n;
        cin >> n;
        vector<int> su1(n);
        for (int i = 0; i < n; ++i) {
            cin >> su1[i];
        }

        int m;
        cin >> m;
        vector<int> su2(m);
        for (int i = 0; i < m; ++i) {
            cin >> su2[i];
        }

        sort(su1.begin(), su1.end());

        for (int i = 0; i < m; ++i) {
            if (binary_search(su1.begin(), su1.end(), su2[i])) {
                cout << "1\n";
            } else {
                cout << "0\n";
            }
        }
    }

    return 0;
}