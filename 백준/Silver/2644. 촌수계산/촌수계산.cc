#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<int> visited;

void dfs(int cur, int goal) {
    if (cur == goal)
        return;

    for (int x : graph[cur]) {
        if (visited[x] == -1) {
            visited[x] = visited[cur] + 1;
            dfs(x, goal);
        }
    }

    return;
}

int main(void) {
    int n;
    int p1, p2;
    int m;
    cin >> n;
    cin >> p1 >> p2;
    p1--;
    p2--;
    cin >> m;

    graph.resize(n);
    visited.resize(n, -1);

    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        x--;
        y--;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    visited[p1] = 0;
    dfs(p1, p2);

    cout << visited[p2] << "\n";
    return 0;
}