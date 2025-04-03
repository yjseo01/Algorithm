#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<vector<int>> rotateVec(vector<vector<int>>& vec, int n, int m);

int main()
{
	int n, m, r, k;
	cin >> n >> m >> r;
	n > m ? k = n : k = m;
	vector<vector<int>> vec(n, vector<int>(m, 0));
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			cin >> vec[i][j];
	}
	
	for (int i = 0; i < r; i++)
		vec = rotateVec(vec, n, m);

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			cout << vec[i][j] << " ";
		cout << "\n";
	}

	return 0;
}

vector<vector<int>> rotateVec(vector<vector<int>>& vec, int n, int m)
{
	vector<vector<int>> tmp(n, vector<int> (m, 0));

	for (int span = 0; span < min(n, m) / 2; span++)
	{
		int top = span, bottom = n - span - 1;
		int left = span, right = m - span - 1;

		// ↓
		for (int i = top; i < bottom; i++)
			tmp[i + 1][left] = vec[i][left];
		// →
		for (int i = left; i < right; i++)
			tmp[bottom][i + 1] = vec[bottom][i];
		// ↑
		for (int i = bottom; i > top; i--)
			tmp[i - 1][right] = vec[i][right];
		// ←
		for (int i = right; i > left; i--)
			tmp[top][i - 1] = vec[top][i];
	}

	return tmp;
}