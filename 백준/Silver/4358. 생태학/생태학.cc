#include <iostream>
#include <map>
#include <string>
#include <iomanip>
#define MAX_SPECIES 10001
#define MAX_TREE 1000001
using namespace std;

int main()
{
	map<string, int> trees;
	long long cnt = 0;

	string line;
	while (getline(cin, line))
	{
		if (cin.eof()) break;
		trees[line]++;
		cnt++;
	}

	int sz = trees.size();
	for (auto it = trees.begin(); it != trees.end(); ++it)
		cout << it->first << " " << fixed << setprecision(4) << it->second * 100.0 / cnt << endl;

	return 0;
}