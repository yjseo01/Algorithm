#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool visited[51] = { false };
string seq;
int s_len;
int n;

vector<int> seq_v;

void backtracking(int depth)
{
    if (depth == s_len)
    {
        for (int x : seq_v)
            cout << x << " ";
        cout << "\n";
        exit(0);
    }

    // 1자리 수
    if (depth < s_len)
    {
        int num = seq[depth] - '0';
        if (num >= 1 && num <= n && !visited[num])
        {
            visited[num] = true;
            seq_v.push_back(num);
            backtracking(depth + 1);
            visited[num] = false;
            seq_v.pop_back();
        }
    }

    // 2자리 수
    if (depth + 1 < s_len)
    {
        string n_str = seq.substr(depth, 2);
        int num = stoi(n_str);
        if (num >= 1 && num <= n && !visited[num])
        {
            visited[num] = true;
            seq_v.push_back(num);
            backtracking(depth + 2);
            visited[num] = false;
            seq_v.pop_back();
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> seq;
    s_len = seq.length();
    n = (s_len < 10) ? s_len : (s_len - 9) / 2 + 9;

    backtracking(0);

    return 0;
}
