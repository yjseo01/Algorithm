#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<int> visited;

int dfs(int x) {
    visited[x] = 1;
    int count = 1;

    for (int node : graph[x]) {
        if (visited[node] == 0)
            count += dfs(node);
    }

    return count;
}

int main(void) {
    int n, m;
    cin >> n;
    cin >> m;

    graph.resize(n);
    visited.resize(n, 0);

    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        x--;
        y--;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    if (m == 0)
        cout << "0\n";
    else
        cout << dfs(0) - 1 << "\n";

    return 0;
}