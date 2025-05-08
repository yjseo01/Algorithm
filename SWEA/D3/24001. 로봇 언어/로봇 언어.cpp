#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

int max_len;
int dp[51][102];

void backtracking(const string& input, int depth, int goal, int cur_len)
{ 
    if (dp[depth][cur_len + 50] != 0)
        return;
    else 
        dp[depth][cur_len + 50] = 1;
    
    max_len = max(max_len, abs(cur_len));
    
    if (depth == goal)
        return;
    
    if (input[depth] == '?')
    {
        backtracking(input, depth + 1, goal, cur_len + 1);
        backtracking(input, depth + 1, goal, cur_len - 1);
    }
    else
    {
        if (input[depth] == 'L')
            cur_len -= 1;
        else 
            cur_len += 1;
        backtracking(input, depth + 1, goal, cur_len);
    }
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        string input;
        cin >> input;
        max_len = 0;
        memset(dp, 0, sizeof(dp));
        backtracking(input, 0, input.length(), 0);
        cout << max_len << "\n";
	}
	return 0;
}