#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;

    int arr[1001];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int dp[1001];
    for (int i = 0; i < n; i++) {
        dp[i] = 1001;
    }

    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < arr[i] + 1; j++) {
            if (i + j < n)
                dp[i + j] = min(dp[i + j], dp[i] + 1);
            else
                break;
        }
    }

    if (dp[n - 1] == 1001)
        cout << "-1\n";
    else
        cout << dp[n - 1] << "\n";

    return 0;
}