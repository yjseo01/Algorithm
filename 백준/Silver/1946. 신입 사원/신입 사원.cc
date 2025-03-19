#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t > 0)
	{
		int n;
		int x, y; // 서류, 면접 순위
		t--;
		cin >> n;
		vector<pair<int, int>> rank;

		for (int i = 0; i < n; i++)
		{
			cin >> x >> y;
			rank.push_back({ x, y });
		}

		sort(rank.begin(), rank.end(),
			[](pair<int, int> a, pair<int, int> b) -> bool {return a.first < b.first;});

		int min_rank = rank[0].second;
		int cnt = 1;
		for (int i = 1; i < n; i++)
		{
			// i번째 지원자의 면접 순위가 지금까지의 면접 순위보다 높으면
			if (min_rank > rank[i].second) 
			{
				min_rank = rank[i].second;
				cnt += 1;
			}
		}

		cout << cnt << "\n";
	}

	return 0;
}