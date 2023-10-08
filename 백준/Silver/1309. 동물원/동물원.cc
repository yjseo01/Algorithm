#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    long long dp[100001];
    dp[1] = 3;
    dp[0] = 1;

    for (int i = 2; i < n + 1; i++)
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901;

    cout << dp[n] << "\n";

    return 0;
}
