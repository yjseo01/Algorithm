#include <iostream>

using namespace std;

int main(void) {
    int n;
    int arr[100001];
    int dp[100001][2];

    int min_idx = 0;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    dp[0][0] = arr[0];
    dp[0][1] = arr[0];
    int ans = arr[0];

    for (int i = 1; i < n; i++) {
        dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i]);
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i]);
        ans = max(ans, max(dp[i][0], dp[i][1]));
    }

    cout << ans << "\n";
    return 0;
}