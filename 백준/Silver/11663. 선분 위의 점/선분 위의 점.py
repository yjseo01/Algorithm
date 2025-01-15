import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()

for _ in range(m):
    x, y = map(int, input().split())

    start_idx = bisect.bisect_left(dot, x)
    end_idx = bisect.bisect_right(dot, y)

    print(end_idx - start_idx)