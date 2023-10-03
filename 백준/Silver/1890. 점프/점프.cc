#include <iostream>
#include <vector>

using namespace std;

int n;
vector<vector<int>> matrix;
vector<vector<long long>> dp;

long long dp_func(int x, int y) {
    int value = matrix[x][y];

    if (x == n - 1 && y == n - 1)
        return 1;

    if (x > n || y > n)
        return 0;

    if (dp[x][y] != -1)
        return dp[x][y];

    dp[x][y] = 0;

    if (x + value < n)
        dp[x][y] += dp_func(x + value, y);

    if (y + value < n)
        dp[x][y] += dp_func(x, y + value);

    return dp[x][y];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    matrix.resize(n, vector<int>(n));
    dp.resize(n, vector<long long>(n, -1));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            cin >> matrix[i][j];
    }

    cout << dp_func(0, 0) << "\n";

    return 0;
}