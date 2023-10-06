#include <iostream>

using namespace std;

int coins[101];
int dp[10001] = {
    0,
};

int main() {
    int n, k;
    cin >> n >> k;

    for (int i = 0; i < n; i++)
        cin >> coins[i];

    dp[0] = 1;

    for (int i = 0; i < n; i++) {
        for (int j = coins[i]; j <= k; j++)
            dp[j] += dp[j - coins[i]];
    }

    cout << dp[k] << "\n";

    return 0;
}
