import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = arr[:n // 2]
right = arr[n // 2:]

lsums = []
rsums = []

for i in range(len(left) + 1):
    for c in combinations(left, i):
        lsums.append(sum(c))
lsums.sort()

for i in range(len(right) + 1):
    for c in combinations(right, i):
        rsums.append(sum(c))
rsums.sort()

lsums_len = len(lsums)
rsums_len = len(rsums)

count = 0
lptr, rptr = 0, rsums_len - 1

while lptr < lsums_len and rptr >= 0:
    lsum, rsum = lsums[lptr], rsums[rptr]
    tsum = lsum + rsum

    if tsum < s:
        lptr += 1
    elif tsum == s:
        duplecnt_l, duplecnt_r = 0, 0
        while lptr < lsums_len and lsums[lptr] == lsum:
            duplecnt_l += 1
            lptr += 1
        while rptr >= 0 and rsums[rptr] == rsum:
            duplecnt_r += 1
            rptr -= 1

        count += duplecnt_l * duplecnt_r

    elif tsum > s:
        rptr -= 1

if s == 0:
    print(count - 1)
else:
    print(count)
