#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int n, k;
	cin >> n >> k;
	vector<int> frame;
	vector<int> recommended(k, 0);
	for (int i = 0; i < k; i++)
		cin >> recommended[i];
	int hash[101] = { 0, }; // 학생의 추천 횟수 저장
	int timestamp[101] = { 0, };
	
	int time = 0;
	for (int i = 0; i < k; i++)
	{
		int student = recommended[i];

		// 이미 액자에 있는 경우 추천 횟수 증가
		auto it = find(frame.begin(), frame.end(), student);
		if (it != frame.end())
		{
			hash[student]++;
			continue;
		}

		// 액자에 공간이 있는 경우 추가
		if (frame.size() < n)
		{
			frame.push_back(student);
			hash[student] = 1;
			timestamp[student] = time++;
			continue;
		}

		// 삭제할 학생 선택
		int min_idx = 0;
		for (int j = 0; j < n; j++)
		{
			// 추천 횟수가 적음 || (추천 횟수가 동일 && 먼저 들어온 학생)
			if (hash[frame[j]] < hash[frame[min_idx]]
				|| (hash[frame[j]] == hash[frame[min_idx]] && timestamp[frame[j]] < timestamp[frame[min_idx]]))
					min_idx = j;
		}

		int r_student = frame[min_idx];
		hash[r_student] = 0; // 추천된 횟수 초기화
		frame[min_idx] = student;
		hash[student] = 1;
		timestamp[student] = time++;
	}

	sort(frame.begin(), frame.end());
	for (int f : frame)
		cout << f << " ";
	cout << "\n";

	return 0;
}