import sys
import bisect
from collections import deque
input = sys.stdin.readline

n, s = map(int, input().split())
cnt = 0

xlist = list(map(int, input().split()))
hlist = list(map(int, input().split()))
xtuplist = [(i, xlist[i]) for i in range(n)]

# bfs
visited = [False for _ in range(n + 1)]
visited[s - 1] = True
queue = deque([s - 1])
xtuplist.sort(key = lambda x : x[1])
xsorted = [x for _, x in xtuplist]

while queue:
    cur = queue.popleft()
    cx = xlist[cur]
    ch = hlist[cur]

    start = 0
    end = n - 1

    left = bisect.bisect_left(xsorted, cx - ch)
    right = bisect.bisect_right(xsorted, cx + ch)

    for i in range(left, right):
        idx = xtuplist[i][0]
        if not visited[idx]:
            visited[idx] = True
            queue.append(idx)

for b in visited:
    if b:
        cnt += 1

for i in range(n):
    if visited[i]:
        print(i + 1, end=" ")
print("")