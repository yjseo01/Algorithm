from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if n >= k:
    print(n - k)
    print(1)
else:
    queue = deque([n])
    dist = [-1] * (2 * k + 1)
    cnt = [0] * (2 * k + 1)
    dist[n] = 0
    cnt[n] = 1

    while queue:
        x = queue.popleft()

        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < 2 * k + 1:
                if dist[nx] == -1:
                    queue.append(nx)
                    dist[nx] = dist[x] + 1
                    cnt[nx] = cnt[x]
                else:
                    if dist[nx] == dist[x] + 1:
                        cnt[nx] += cnt[x]

    print(dist[k])
    print(cnt[k])
