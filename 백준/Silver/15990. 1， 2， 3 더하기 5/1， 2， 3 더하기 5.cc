#include <iostream>
#include <vector>
#define MAX 100000
#define MOD 1000000009

using namespace std;

int main() {
    int t;
    cin >> t;

    vector<vector<unsigned long long>> dp(MAX + 1,
                                          vector<unsigned long long>(4, 0));

    dp[1][1] = 1;
    dp[2][2] = 1;
    dp[3][1] = 1;
    dp[3][2] = 1;
    dp[3][3] = 1;

    while (t-- > 0) {
        long long n;
        cin >> n;

        for (int i = 4; i < n + 1; i++) {
            dp[i][1] = (dp[i - 1][3] + dp[i - 1][2]) % MOD;
            dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD;
            dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD;
        }

        cout << ((dp[n][1] + dp[n][2] + dp[n][3]) % MOD) << "\n";
    }

    return 0;
}