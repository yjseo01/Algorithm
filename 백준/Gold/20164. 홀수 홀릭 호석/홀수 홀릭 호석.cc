#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int total_max = 0, total_min = 1e9;

int countOddDigits(int num) {
	int cnt = 0;
	while (num > 0) {
		if ((num % 10) % 2 == 1) cnt++;
		num /= 10;
	}
	return cnt;
}

void countOdd(int num, int oddCnt) {
	int cnt = countOddDigits(num);
	oddCnt += cnt;

	if (num < 10) {
		total_min = min(total_min, oddCnt);
		total_max = max(total_max, oddCnt);
		return;
	}
	else if (num < 100) {
		int a = num / 10;
		int b = num % 10;
		countOdd(a + b, oddCnt);
	}
	else {
		string s = to_string(num);
		int n_len = s.length();

		for (int i = 1; i < n_len - 1; i++) {
			for (int j = i + 1; j < n_len; j++) {
				int a = stoi(s.substr(0, i));
				int b = stoi(s.substr(i, j - i));
				int c = stoi(s.substr(j));

				countOdd(a + b + c, oddCnt);
			}
		}
	}
}

int main() {
	int n; cin >> n;
	countOdd(n, 0);
	cout << total_min << " " << total_max << "\n";
	return 0;
}
