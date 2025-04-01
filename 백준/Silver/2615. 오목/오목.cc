#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<vector<int>> board(19, vector<int>(19, 0));
	for (int i = 0; i < 19; i++)
		for (int j = 0; j < 19; j++)
			cin >> board[i][j];

	// → ↓ ↘ ↗
	int dx[4] = { 1, 0, 1, 1 };
	int dy[4] = { 0, 1, 1, -1 };

	for (int y = 0; y < 19; y++)
	{
		for (int x = 0; x < 19; x++)
		{
			if (board[y][x] == 0)
				continue;
			int color = board[y][x];
			for (int i = 0; i < 4; i++) // → ↓ ↘ ↗
			{
				int cnt = 1;
				int nx = x + dx[i], ny = y + dy[i];
				while (cnt < 5 
					&& 0 <= nx && nx < 19
					&& 0 <= ny && ny < 19)
				{
					if (board[ny][nx] != color)
						break;
					cnt++;
					nx = x + dx[i] * cnt;
					ny = y + dy[i] * cnt;
				}

				if (cnt < 5)
					continue;

				// 육목 체크
				if (0 <= nx && nx < 19
					&& 0 <= ny && ny < 19)
				{
					if (board[ny][nx] == color)
						continue;
				}

				int prev_x = x - dx[i], prev_y = y - dy[i];
				if (0 <= prev_x && prev_x < 19
					&& 0 <= prev_y && prev_y < 19)
				{
					if (board[prev_y][prev_x] == color)
						continue;
				}

				// 오목
				cout << color << "\n";
				cout << y + 1 << " " << x + 1 << "\n";
				return 0;
			}
		}
	}

	cout << 0 << "\n";
	return 0;
}