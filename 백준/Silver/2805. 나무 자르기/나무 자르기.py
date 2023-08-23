import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().rsplit()))

high = max(trees)
low = 0
mid = 0
ans = 0
while low <= high:
    mid = (high + low) // 2
    length = 0
    for t in trees:
        if t > mid:
            length += t - mid

    if length >= M:
        low = mid + 1
        ans = mid
    else:
        high = mid - 1

print(ans)