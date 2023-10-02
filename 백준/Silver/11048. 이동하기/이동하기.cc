#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> maze(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            cin >> maze[i][j];
    }

    vector<vector<int>> dp(n, vector<int>(m, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {

            if (i == 0 && j == 0) {
                dp[i][j] = maze[0][0];
                continue;
            }

            if (i > 0 && j > 0) {
                if (dp[i][j] < dp[i - 1][j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
            }

            if (i > 0) {
                if (dp[i][j] < dp[i - 1][j])
                    dp[i][j] = dp[i - 1][j];
            }

            if (j > 0) {
                if (dp[i][j] < dp[i][j - 1])
                    dp[i][j] = dp[i][j - 1];
            }

            dp[i][j] += maze[i][j];
        }
    }

    cout << dp[n - 1][m - 1] << "\n";

    return 0;
}
