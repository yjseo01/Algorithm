#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int n, k;
vector<string> words;
bool alpha[26];
int ans;

void dfs(int idx, int left)
{
	if (!left) // 종료조건: k - 5개 학습 완료
	{
		// 읽을 수 있는 단어 세기
		int cnt = 0;
		for (string word : words)
		{
			bool is_readable = true;
			for (char c : word)
			{
				if (!alpha[c - 'a'])
				{
					is_readable = false;
					break;
				}
			}

			if (is_readable)
				cnt += 1;
		}

		if (cnt == n)
		{
			cout << cnt << "\n";
			exit(0);
		}

		ans = max(ans, cnt);
	}
	else
	{
		for (int i = idx; i < 26; i++)
		{
			if (!alpha[i])
			{
				alpha[i] = true;
				dfs(i, left - 1);
				alpha[i] = false;
			}
		}
	}
}

int main()
{
	cin >> n >> k; // 0 < n <= 50, 0 <= k <= 26

	string str = "";
	for (int i = 0; i < n; i++)
	{
		cin >> str;
		words.push_back(str.substr(4, str.length() - 8));
	}

	if (k < 5) // a c i n t
	{
		cout << 0 << "\n";
		return 0;
	}

	alpha[0] = true;
	alpha['c' - 'a'] = true;
	alpha['i' - 'a'] = true;
	alpha['n' - 'a'] = true;
	alpha['t' - 'a'] = true;

	dfs(0, k - 5);
	cout << ans << "\n";
	return 0;

}