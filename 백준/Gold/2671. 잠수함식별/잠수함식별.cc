#include <iostream>
#include <vector>

using namespace std;

int main()
{
	// (100~1~|01)~
	string sound;

	while (cin >> sound)
	{
		int idx = 0;
		int len = sound.length();

		while (idx != len)
		{
			// 01
			if (idx + 1 < len && sound[idx] == '0' && sound[idx + 1] == '1')
			{
				idx += 2;
			}
			// 100
			else if (idx + 3 < len && sound[idx] == '1' && sound[idx + 1] == '0' && sound[idx + 2] == '0')
			{
				idx += 3;
				// 0~
				while (idx < len && sound[idx] == '0') idx++;
				if (idx >= len) // 10...0
				{
					cout << "NOISE\n";
					return 0;
				}

				// 1~
				while (idx < len && sound[idx] == '1') idx++;
			}
			else
			{
				if (idx - 2 > 0 && sound[idx - 2] == '1' && sound[idx - 1] == '1' && sound[idx] == '0') // ...1 10
				{
					idx -= 1;
				}
				else
				{
					cout << "NOISE\n";
					return 0;
				}
			}
		}

		cout << "SUBMARINE\n";
	}
	return 0;
}