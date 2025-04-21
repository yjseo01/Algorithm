#include <iostream>

using namespace std;

// pseudo palindrome
int isPalindrome(const string& str)
{
	int start = 0, end = str.length() - 1;
	bool isRemoved = false;
	while (start < end)
	{
		// cout << "start, end: " << str[start] << " " << str[end] << "\n";
		// cout << start << " " << end << "\n";
		if (str[start] == str[end])
		{
			start++;
			end--;
		}
		else // 회문 조건에 맞지 않는 문자를 발견
		{
			if (isRemoved) // 이미 문자 한 개 삭제
				return 2;

			int s, e;
			// start + 1 삭제하기
			bool delStart = true;
			s = start + 1;
			e = end;
			
			while (s < e)
			{
				if (str[s++] != str[e--])
				{
					delStart = false;
					break;
				}
			}

			// end - 1 삭제하기
			bool delEnd = true;
			s = start;
			e = end - 1;

			while (s < e)
			{
				if (str[s++] != str[e--])
				{
					delEnd = false;
					break;
				}
			}

			if (!delStart && !delEnd)
				return 2;
			else
				return 1;
		}
	}

	if (start >= end)
	{
		if (isRemoved)
			return 1;
		else
			return 0;
	}
}

int main()
{
	//  회문 0, 유사 회문 1, 회문 아님 2
	int t;
	cin >> t;

	while (t-- > 0)
	{
		string str;
		cin >> str;
		
		cout << isPalindrome(str) << "\n";
	}

	return 0;
}