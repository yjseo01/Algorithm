#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int n, s, r, num;
	int cnt = 0; // 출발을 할 수 없는 팀의 최솟값

	cin >> n >> s >> r;
	vector<int> boats(n + 1, 1);
	
	for (int i = 0; i < s; i++) // 카약이 손상된 팀
	{
		cin >> num;
		boats[num] -= 1;
	}

	for (int i = 0; i < r; i++) // 카약을 하나 더 가져온 팀
	{
		cin >> num;
		boats[num] += 1;
	}

	for (int i = 1; i < n + 1; i++)
	{
		if (boats[i] == 2)
		{
			if (i - 1 >= 1 && boats[i - 1] == 0)
			{
				boats[i - 1] += 1;
				boats[i] -= 1;
			}
			else if (i + 1 < n + 1 && boats[i + 1] == 0)
			{
				boats[i + 1] += 1;
				boats[i] -= 1;
			}
		}
	}

	for (int i = 0; i < n + 1; i++)
	{
		if (boats[i] == 0)
			cnt += 1;
	}

	cout << cnt << "\n";
	return 0;
}