#include <iostream>

using namespace std;

int main()
{
    int n, s;
    cin >> n >> s;
    int arr[n + 1];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int length = 1;
    int min_length = n + 1;
    int sum = arr[0];
    int start = 0;
    int end = 0;
    
    while(start <= end && end < n) {
        if (sum < s) {
            sum += arr[++end];
            length++;
        } else if (sum >= s) {
            if (min_length > length) {
                min_length = length;
            }
            
            sum -= arr[start++];
            length -= 1;
            
            if (start > end) {
                end = start;
                sum = arr[start];
                length = 1;
            }
        }
    }
    
    if (min_length == n + 1) {
        cout << 0 << "\n";
    } else {
        cout << min_length << "\n";
    }

    return 0;
}