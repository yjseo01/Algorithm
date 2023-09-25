#include <iostream>
#include <math.h>
#include <vector>
#define MAX 2000

using namespace std;

bool isPrimeNum(int x) {
    int x_sqrt = (int)sqrt(x);
    for (int i = 2; i <= x_sqrt; i++) {
        if (x % i == 0)
            return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;

    if (n == 1) {
        cout << "0\n";
    } else {
        vector<int> primes;
        primes.reserve(n);
        int primes_length = 0;

        for (int i = 2; i < n + 1; i++) {
            if (isPrimeNum(i))
                primes.push_back(i);
        }

        int start = 0;
        int end = 0;
        int sum = 2;
        int cnt = 0;

        while (start <= end && end < primes.size()) {
            if (sum < n) {
                sum += primes[++end];
            } else if (sum == n) {
                cnt += 1;
                sum += primes[++end];
            } else if (sum > n) {
                sum -= primes[start++];

                if (start > end && start < primes.size()) {
                    end = start;
                    sum = primes[start];
                }
            }
        }

        cout << cnt << "\n";
    }

    return 0;
}
