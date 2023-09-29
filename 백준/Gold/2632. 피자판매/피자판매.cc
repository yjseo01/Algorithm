#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> get_sum(int x, vector<int> v) {
    vector<int> sumvec;
    sumvec.push_back(0);

    for (int i = 0; i < x; i++) {
        int sum = 0;
        for (int j = i; j < i + x - 1; j++) {
            sum += v[j % x];
            sumvec.push_back(sum);
        }
    }

    int sum = 0;
    for (int i = 0; i < x; i++) {
        sum += v[i];
    }
    sumvec.push_back(sum);

    return sumvec;
}

int main() {
    int pizza_size;
    int m, n;
    cin >> pizza_size;
    cin >> m >> n;

    vector<int> avec(m);
    vector<int> bvec(n);

    for (int i = 0; i < m; i++) {
        cin >> avec[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> bvec[i];
    }

    vector<int> asumvec;
    vector<int> bsumvec;
    asumvec = get_sum(m, avec);
    bsumvec = get_sum(n, bvec);
    int len_asumvec = asumvec.size();
    int len_bsumvec = bsumvec.size();

    sort(asumvec.begin(), asumvec.end());
    sort(bsumvec.begin(), bsumvec.end());

    int start = 0, end = len_bsumvec - 1;
    int cnt = 0;
    int asum = 0, bsum = 0, tsum = 0;

    while (start < len_asumvec && end >= 0) {
        asum = asumvec[start];
        bsum = bsumvec[end];
        tsum = asum + bsum;

        if (tsum < pizza_size)
            start++;
        else if (tsum == pizza_size) {
            int dupleA = 0, dupleB = 0;

            while (start < len_asumvec && asumvec[start] == asum) {
                start++;
                dupleA++;
            }

            while (end >= 0 && bsumvec[end] == bsum) {
                end--;
                dupleB++;
            }

            cnt += dupleA * dupleB;
        } else
            end--;
    }

    cout << cnt << "\n";

    return 0;
}
