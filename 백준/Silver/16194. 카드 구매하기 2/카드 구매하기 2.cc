#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    int prices[1001];
    int dp[1001];
    dp[0] = 0;
    
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
        dp[i + 1] = prices[i];
    }
    
    for (int i = 2; i < n + 1; i++) {
        for (int j = 1; j < i; j++)
            dp[i] = min(dp[i], dp[i - j] + prices[j - 1]);
    }
    
    cout << dp[n] << "\n";
    
    return 0;
}