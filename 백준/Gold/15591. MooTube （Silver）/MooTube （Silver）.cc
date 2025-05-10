#include <iostream>
#include <algorithm>
#include <climits>
#include <vector>
#include <queue>

using namespace std;

int N, Q;

int bfs(vector<vector<pair<int, int>>>& graph, int v, long long k)
{
    int cnt = 0;
    vector<bool> visited(N + 1, false);
    queue<pair<int, long long>> q;

    q.push({v, k});
    visited[v] = true;

    while(!q.empty())
    {
        int v = q.front().first;
        long long vcost = q.front().second;
        q.pop();

        for (int i = 0; i < graph[v].size(); i++)
        {
            int nv = graph[v][i].first;
            long long ecost = graph[v][i].second;
            long long ncost = min(ecost, vcost);

            if (!visited[nv] && ncost >= k)
            {
                visited[nv] = true;
                cnt++;
                q.push({nv, ncost});
            }
        }
    }

    return cnt;
}

int main()
{
    cin >> N >> Q;
    vector<vector<pair<int, int>>> graph(N + 1);
    vector<int> ans(Q, 0);

    for (int i = 0; i < N - 1; i++)
    {
        int a, b, usado;
        cin >> a >> b >> usado;
        graph[a].push_back({b, usado});
        graph[b].push_back({a, usado});
    }

    for (int i = 0; i < Q; i++)
    {
        int v;
        long long k;
        cin >> k >> v;
        ans[i] = bfs(graph, v, k);
    }

    for (int i = 0; i < Q; i++)
    {
        cout << ans[i] << "\n";
    }

    return 0;
}