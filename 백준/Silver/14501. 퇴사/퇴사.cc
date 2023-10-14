#include <iostream>
#define MAX 15
using namespace std;

int main() {
    int t[MAX + 1] = {
        0,
    };
    int p[MAX + 1]{
        0,
    };
    int dp[MAX + 1] = {
        0,
    };

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> t[i] >> p[i];

    int max_money = 0;

    for (int i = 0; i < n + 1; i++) {
        dp[i] = max(max_money, dp[i]);

        if (t[i] + i < n + 1)
            dp[t[i] + i] = max(dp[t[i] + i], p[i] + dp[i]);

        max_money = max(max_money, dp[i]);
    }

    cout << max_money << "\n";

    return 0;
}