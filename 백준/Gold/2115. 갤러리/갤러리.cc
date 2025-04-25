#include <iostream>
#include <vector>

using namespace std;

bool visited[1001][1001][4] = {false};

int main()
{
	int m, n;
	cin >> m >> n;
	vector<string> vec(m);
	for (int i = 0; i < m; i++)
	{
		string str;
		cin >> str;
		vec[i] = str;
	}

	int cnt = 0;

	for (int y = 1; y < m - 1; y++)
	{
		for (int x = 1; x < n - 1; x++)
		{
			// 가로
			if (vec[y][x] == '.' && vec[y][x + 1] == '.')
			{
				if (y + 1 < m && vec[y + 1][x] == 'X' && vec[y + 1][x + 1] == 'X')
				{
					if (!visited[y][x][0] && !visited[y][x + 1][0])
					{
						cnt++;
						visited[y][x][0] = true;
						visited[y][x + 1][0] = true;
					}
				}

				if (y - 1 >= 0 && vec[y - 1][x] == 'X' && vec[y - 1][x + 1] == 'X')
				{
					if (!visited[y][x][1] && !visited[y][x + 1][1])
					{
						cnt++;
						visited[y][x][1] = true;
						visited[y][x + 1][1] = true;
					}
				}
			}

			// 세로
			if (vec[y][x] == '.' && vec[y + 1][x] == '.')
			{
				if (x + 1 < n && vec[y][x + 1] == 'X' && vec[y + 1][x + 1] == 'X')
				{
					if (!visited[y][x][2] && !visited[y + 1][x][2])
					{
						cnt++;
						visited[y][x][2] = true;
						visited[y + 1][x][2] = true;
					}
				}

				if (x - 1 >= 0 && vec[y][x - 1] == 'X' && vec[y + 1][x - 1] == 'X')
				{
					if (!visited[y][x][3] && !visited[y + 1][x][3])
					{
						cnt++;
						visited[y][x][3] = true;
						visited[y + 1][x][3] = true;
					}
				}
			}
		}
	}

	cout << cnt << "\n";
	return 0;
}