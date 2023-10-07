#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> costs(n, vector<int>(3));
    vector<vector<int>> dp(n, vector<int>(3, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++)
            cin >> costs[i][j];
    }

    dp[0][0] = costs[0][0];
    dp[0][1] = costs[0][1];
    dp[0][2] = costs[0][2];

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            if (j == 0)
                dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]);
            else if (j == 1)
                dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]);
            else
                dp[i][j] = min(dp[i - 1][1], dp[i - 1][0]);

            dp[i][j] += costs[i][j];
        }
    }

    int ans = dp[n - 1][0];
    for (int j = 1; j < 3; j++) {
        if (ans > dp[n - 1][j])
            ans = dp[n - 1][j];
    }
    cout << ans << "\n";

    return 0;
}
