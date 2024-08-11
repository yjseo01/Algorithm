from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if n >= k:
    print(n - k)
else:
    queue = deque([n])
    dist = [-1] * (2 * k + 1)
    dist[n] = 0

    while queue:
        x = queue.popleft()

        for nx in (x + 1, x - 1, 2 * x):
            if 0 <= nx < 2 * k + 1:
                if dist[nx] == -1:
                    queue.append(nx)

                    if nx == 2 * x:
                        dist[nx] = dist[x]
                    else:
                        dist[nx] = dist[x] + 1
                else:
                    if nx == 2 * x:
                        dist[nx] = min(dist[nx], dist[x])
                    else:
                        dist[nx] = min(dist[nx], dist[x] + 1)

    print(dist[k])
