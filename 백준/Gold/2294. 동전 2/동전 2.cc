#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> coins(n);
    vector<int> dp(k + 1, -1);

    for (int i = 0; i < n; i++) {
        cin >> coins[i];
        if (coins[i] <= k)
            dp[coins[i]] = 1;
    }

    for (int i = 0; i <= k; i++) {
        for (int j = 0; j < i / 2 + 1; j++) {
            if (dp[i - j] != -1 && dp[j] != -1) {
                if (dp[i] > 0)
                    dp[i] = min(dp[i], dp[i - j] + dp[j]);
                else
                    dp[i] = dp[i - j] + dp[j];
            }
        }
    }

    cout << dp[k] << "\n";

    return 0;
}
