#include <iostream>

using namespace std;

int n;
int graph[101][101];
int visited[101][101];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void dfs(int x, int y, int h) {
    visited[x][y] = 1;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (0 <= nx && nx < n && 0 <= ny && ny < n) {
            if (visited[nx][ny] == 0 && graph[nx][ny] >= h) {
                dfs(nx, ny, h);
            }
        }
    }
}

int main(void) {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
            visited[i][j] = 0;
        }
    }

    int ans = 0;
    int cnt = 0;

    for (int i = 1; i < 101; i++) { // 높이
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                visited[j][k] = 0;
            }
        }

        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (visited[j][k] == 0 && graph[j][k] >= i) {
                    dfs(j, k, i);
                    cnt++;
                }
            }
        }

        if (cnt == 0)
            break;

        if (ans < cnt)
            ans = cnt;

        cnt = 0;
    }

    cout << ans << "\n";

    return 0;
}