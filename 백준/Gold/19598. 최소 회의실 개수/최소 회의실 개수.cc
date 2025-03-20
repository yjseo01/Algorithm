#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int n;
	vector<pair<int, int>> meetings;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int start, end;
		cin >> start >> end;
		meetings.push_back({ start, end });
	}

	sort(meetings.begin(), meetings.end(), [](pair<int, int> p1, pair<int, int> p2) -> bool {return p1.first < p2.first;});

	vector<int> meeting_room = {meetings[0].second};
	int cnt = 1;
	for (int i = 1; i < n; i++)
	{
		bool is_end = false;
		for (int j = 0; j < cnt; j++)
		{
			if (meeting_room[j] <= meetings[i].first) // 새로운 회의실 필요 없음
			{
				meeting_room[j] = meetings[i].second; // 마지막 회의가 끝나는 시간 갱신
				is_end = true;
				break;
			}
		}

		if (!is_end)
		{
			cnt += 1;
			meeting_room.push_back(meetings[i].second);
		}
	}

	cout << cnt << "\n";

	return 0;
}