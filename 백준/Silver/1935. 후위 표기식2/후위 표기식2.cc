#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main()
{
	int n;
	string postfix;
	vector<double> stack;
	cin >> n >> postfix;
	vector<int> vals(n, 0);
	for (int i = 0; i < n; i++)
		cin >> vals[i];

	double x, y;
	for (char c : postfix)
	{
		if (65 <= c && c <= 90) // ABC...Z
		{
			stack.push_back((double)vals[c - 65]);
		}
		else // +-*/
		{
			y = stack.back();
			stack.pop_back();
			x = stack.back();
			stack.pop_back();

			switch (c)
			{
			case '+':
				stack.push_back(x + y);
				break;
			case '-':
				stack.push_back(x - y);
				break;
			case '*':
				stack.push_back(x * y);
				break;
			case '/':
				stack.push_back(x / y);
			}
		}
	}

	//cout << stack.back() << "\n";
	cout << fixed << setprecision(2) << stack.back() << "\n";

	return 0;
}