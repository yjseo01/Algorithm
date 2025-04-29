#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
bool visited[25][25];
int cnt;

bool chk_b(int x, int y)
{
	if (0 <= x && x < n && 0 <= y && y < m)
		return true;
	else
		return false;
}

void backtracking(int x, int y)
{
	if (x == n)
	{
		y++;
		x = 0;
	}

	if (y == m)
	{
		cnt++;
		return;
	}

	int nx, ny;
	bool makesNemmo = false;
	if (chk_b(x - 1, y) && chk_b(x, y - 1) && chk_b(x - 1, y - 1))
	{
		if (visited[y][x - 1] && visited[y - 1][x] && visited[y - 1][x - 1])
			makesNemmo = true;
	}

	backtracking(x + 1, y);

	if (!makesNemmo)
	{
		visited[y][x] = true;
		backtracking(x + 1, y);
		visited[y][x] = false;
	}
}

int main()
{
	cin >> n >> m;
	cnt = 0;

	backtracking(0, 0);
	cout << cnt << "\n";
	
	return 0;
}