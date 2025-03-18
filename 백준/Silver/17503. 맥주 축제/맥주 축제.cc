#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int n, m, k;
	vector<pair<long long, long long>> beers;

	cin >> n >> m >> k;
	for (int i = 0; i < k; i++)
	{
		long long v, c; // 선호도, 도수 레벨
		cin >> v >> c;
		beers.push_back({ v, c });
	}

	// 도수 레벨 오름차순 정렬
	sort(beers.begin(), beers.end(), [](pair<long long, long long> p1, pair<long long, long long> p2) -> bool {return p1.second < p2.second;});

	// 간 레벨을 mid라 하고 이분 탐색 시작
	long long ans = 1e13;

	long long low = beers[0].second;
	long long high = beers[k - 1].second;
	long long mid;
	while (low <= high)
	{
		mid = (low + high) / 2;
		
		// 간 레벨(mid) >= 도수 레벨(c)인 술을 벡터에 추가
		vector<long long> candidates;
		for (auto beer : beers)
		{
			if (beer.second <= mid)
				candidates.push_back(beer.first);
		}

		// 가능한 맥주의 종류 개수가 n개보다 작으면 mid값 증가
		if (candidates.size() < n)
		{
			low = mid + 1;
			continue;
		}

		// 가능한 맥주 배열을 선호도 순서대로 정렬하고 상위 n개의 총 선호도 구하기
		long long total = 0;
		sort(candidates.begin(), candidates.end(), [](long long x, long long y) -> bool {return x > y;});
		for (int i = 0; i < n; i++)
			total += candidates[i];

		if (total < m)
		{
			low = mid + 1;
		}
		else // 조건 만족 
		{
			high = mid - 1;
			ans = min(ans, mid);
		}
	}

	cout << (ans == 1e13 ? -1 : ans) << "\n";
	return 0;
}