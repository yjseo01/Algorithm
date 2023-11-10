#include <iostream>

using namespace std;

int main() {
    int n;
    int idx, tmp = 0;
    int ans = 0;
    int arr[1001];
    int dp[1001] = {
        0,
    };
    int ans_arr[1001];

    cin >> n;

    for (int i = 1; i < n + 1; i++) {
        cin >> arr[i];
    }

    dp[1] = 1;

    for (int i = 1; i < n + 1; i++) {
        int max_len = 0;

        for (int j = 1; j < i; j++) {
            if (arr[i] > arr[j])
                max_len = max(dp[j], max_len);
        }

        dp[i] = max_len + 1;

        if (tmp < max_len + 1) {
            tmp = max_len + 1;
            idx = i;
        }
    }

    for (int i = idx; i >= 1; i--) {
        if (dp[i] == tmp) {
            ans_arr[ans++] = arr[i];
            tmp--;
        }
    }

    cout << ans << "\n";
    for (int i = ans - 1; i >= 0; i--) {
        cout << ans_arr[i] << " ";
    }

    return 0;
}