#include <iostream>
#include <vector>

using namespace std;

int lab[2001][2001];
int visited[2001][2001][4];

int main()
{
	int n, m;
	cin >> n >> m;

	//vector<vector<int>> lab(n, vector<int>(m, 0));
	//vector<vector<vector<int>>> visited(n, vector<vector<int>>(m, vector<int>(4, 0)));
	vector<pair<int, int>> aircon;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> lab[i][j];
			if (lab[i][j] == 9)
				aircon.push_back(make_pair(j, i));
		}
	}

	// → ↑ ← ↓
	int dx[4] = { 1, 0, -1, 0 };
	int dy[4] = { 0, -1, 0, 1 };

	vector<vector<int>> counted(n, vector<int>(m, 0));
	int ans = 0;

	for (auto p : aircon)
	{
		int x = p.first, y = p.second;
		if (counted[y][x] == 0)
		{
			counted[y][x] = 1;
			ans++;
		}

		// → ↑ ← ↓
		for (int i = 0; i < 4; i++)
		{
			int nx = x + dx[i], ny = y + dy[i];
			int idx = i; // 방향
			bool isBlocked = false;
			while (0 <= ny && ny < n && 0 <= nx && nx < m)
			{
				if (visited[ny][nx][idx]) break;
				visited[ny][nx][idx] = 1;

				if (counted[ny][nx] == 0)
				{
					counted[ny][nx] = 1;
					ans++;
				}

				switch (lab[ny][nx])
				{
				case 0:
					break;
				case 1:
					if (idx == 0 || idx == 2)
						isBlocked = true;
					break;
				case 2:
					if (idx == 1 || idx == 3)
						isBlocked = true;
					break;
				case 3:
					if (idx == 0) idx = 1;
					else if (idx == 1) idx = 0;
					else if (idx == 2) idx = 3;
					else if (idx == 3) idx = 2;
					break;
				case 4:
					if (idx == 0) idx = 3;
					else if (idx == 1) idx = 2;
					else if (idx == 2) idx = 1;
					else if (idx == 3) idx = 0;
					break;
				case 9:
					break;
				}

				if (isBlocked)
					break;

				nx += dx[idx];
				ny += dy[idx];
			}
		}
	}

	cout << ans << "\n";
}
