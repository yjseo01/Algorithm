#include <iostream>
#define MAX 1000001

using namespace std;

int main(void) {
    int n;
    int arr[3][1001];
    int dp[3][1001];
    int lastColor[3] = {0, 1, 2};
    int ans = MAX;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[0][i] >> arr[1][i] >> arr[2][i];
    }

    for (int i = 0; i < 3; i++) {
        dp[i][0] = arr[i][0];
        if (i == 0) {
            dp[1][0] = MAX;
            dp[2][0] = MAX;
        } else if (i == 1) {
            dp[0][0] = MAX;
            dp[2][0] = MAX;
        } else {
            dp[0][0] = MAX;
            dp[1][0] = MAX;
        }

        for (int j = 1; j < n; j++) {
            dp[0][j] = min(dp[1][j - 1], dp[2][j - 1]) + arr[0][j];
            dp[1][j] = min(dp[0][j - 1], dp[2][j - 1]) + arr[1][j];
            dp[2][j] = min(dp[0][j - 1], dp[1][j - 1]) + arr[2][j];
        }

        for (int j = 0; j < 3; j++) {
            if (j != i) {
                ans = min(ans, dp[j][n - 1]);
            }
        }
    }

    cout << ans << "\n";

    return 0;
}