#include <iostream>

using namespace std;

int main()
{
	string str;
	cin >> str; 

	int start = 0, end = str.length() - 1;
	int idx = 0;


	int s = start, e = end;
	bool isP = true;
	bool isAllSame = true;

	while (s < e) // 펠린드롬인지 확인
	{
		if (str[s] == str[e])
		{
			if (s < e && (str[s] != str[s + 1] ||  str[e] != str[e - 1]))
				isAllSame = false;
			s++;
			e--;
		}
		else
		{
			isP = false;
			break;
		}
	}

	if (isP)
	{
		if (isAllSame) // zzzzzz
		{
			cout << -1 << "\n";
			return 0;
		}
		else
		{
			cout << end - start << "\n";
			return 0;
		}
	}

	cout << end - start + 1 << "\n";

	return 0;
}