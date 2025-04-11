#include <iostream>
#include <queue>
using namespace std;

int arr[100001];

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL);

	int n;
	cin >> n;
	priority_queue<int> pq;

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	int x;
	for (int i = 0; i < n; i++)
	{
		x = arr[i];
		if (x == 0)
		{
			if (pq.empty())
			{
				cout << 0 << "\n";
			}
			else
			{
				cout << pq.top() << "\n";
				pq.pop();
			}
		}
		else
		{
			pq.push(x);
		}
	}

	return 0;
}