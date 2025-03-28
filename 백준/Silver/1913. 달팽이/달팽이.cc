#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    vector<vector<int>> vec(n, vector<int>(n, 0));
    int x = n / 2, y = n / 2;
    vec[y][x] = 1;
    int cur = 2;

    for (int i = 1; i <= n / 2; i++)
    {
        y--; 
        vec[y][x] = cur++;
        for (int j = 0; j < i * 2 - 1; j++) vec[y][++x] = cur++; // →
        for (int j = 0; j < i * 2; j++) vec[++y][x] = cur++; // ↓
        for (int j = 0; j < i * 2; j++) vec[y][--x] = cur++; // ←
        for (int j = 0; j < i * 2; j++) vec[--y][x] = cur++; // ↑
    }

    int kx, ky;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << vec[i][j] << " ";
            if (vec[i][j] == k)
                ky = i, kx = j; 
        }
        cout << "\n";
    }

    cout << ky + 1 << " " << kx + 1 << "\n"; 
    return 0;
}
