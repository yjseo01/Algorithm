#include <iostream>
#define MOD 1000000009
#define MAX 1000000

using namespace std;

int main() {
    long long dp[MAX + 1];
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;

    int t;
    cin >> t;

    while (t > 0) {
        t--;

        int n;
        cin >> n;

        for (int i = 3; i < n + 1; i++)
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD;

        cout << dp[n] << "\n";
    }

    return 0;
}
