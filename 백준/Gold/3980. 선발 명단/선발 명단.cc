#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<vector<int>> tbl;
bool visited[11]{ false };
int max_s;

void backtracking(int pos, int cur_s)
{
	if (pos == 11)
	{
		max_s = max(cur_s, max_s);
		return;
	}

	for (int p = 0; p < 11; p++) // player
	{
		if (!visited[p] && tbl[p][pos] > 0)
		{
			visited[p] = true;
			backtracking(pos + 1, cur_s + tbl[p][pos]);
			visited[p] = false;
		}
	}
}

int main()
{
	int c;
	cin >> c;
	while (c-- > 0)
	{
		tbl = vector<vector<int>>(11, vector<int>(11));
		for (int i = 0; i < 11; i++)
			for (int j = 0; j < 11; j++) cin >> tbl[i][j];

		backtracking(0, 0);

		cout << max_s << "\n";
		max_s = 0;
	}

	return 0;
}