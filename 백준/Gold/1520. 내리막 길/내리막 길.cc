#include <iostream>
#include <vector>

using namespace std;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

int m, n;
vector<vector<int>> map;
vector<vector<int>> dp;

int dp_func(int x, int y) {
    if (x == m - 1 && y == n - 1) // 목적지
        return 1;

    if (dp[x][y] != -1) // 이미 방문
        return dp[x][y];

    dp[x][y] = 0; // 방문 처리

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i], ny = y + dy[i];

        if (0 <= nx && nx < m && 0 <= ny && ny < n) {
            if (map[x][y] > map[nx][ny]) // 내리막길
                dp[x][y] += dp_func(nx, ny);
        }
    }

    return dp[x][y];
}

int main() {

    cin >> m >> n;

    map.resize(m, vector<int>(n));
    dp.resize(m, vector<int>(n, -1));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            cin >> map[i][j];
    }

    int ans = dp_func(0, 0);
    cout << ans << "\n";

    return 0;
}
