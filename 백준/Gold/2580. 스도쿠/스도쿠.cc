#include <iostream>
#include <vector>
using namespace std;

int matrix[9][9];
vector<pair<int, int>> blanks;

bool chk_row(int x, int n) // 가로줄
{
    for (int i = 0; i < 9; i++)
    {
        if (matrix[i][x] == n)
            return false;
    }
    return true;
}

bool chk_col(int y, int n) // 세로줄
{
    for (int i = 0; i < 9; i++)
    {
        if (matrix[y][i] == n)
            return false;
    }

    return true;
}

bool chk_squ(int x, int y, int n) // 3 x 3 정사각형
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (n == matrix[y / 3 * 3 + i][x / 3 * 3 + j])
                return false;
        }
    }

    return true;
}

void backtracking(int depth)
{
    if (depth == blanks.size())
    {
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
                cout << matrix[i][j] << " ";
            cout << "\n";
        }

        exit(0);
    }

    int x, y;
    for (int i = 1; i < 10; i++)
    {
        x = blanks[depth].first, y = blanks[depth].second;
        
        if (chk_col(y, i) && chk_row(x, i) && chk_squ(x, y, i))
        {
            matrix[y][x] = i;
            backtracking(depth + 1);
            matrix[y][x] = 0;
        }
    }

    return;
}

int main()
{
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cin >> matrix[i][j];
            if (matrix[i][j] == 0)
                blanks.push_back({j, i});
        }
    }

    backtracking(0);

    return 0;
}