#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    int arr[n + 1];
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int sum = 0;
    int cnt = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            sum += arr[j];
            
            if (sum == m) {
                cnt++;
                sum = 0;
                break;
            }
        }
        sum = 0;
    }
    
    cout << cnt;
    
    return 0;
}