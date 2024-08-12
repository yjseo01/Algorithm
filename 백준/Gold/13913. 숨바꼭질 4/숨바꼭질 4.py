from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
path = []

if n >= k:
    for i in range(k, n + 1):
        path.append(i)
    path.reverse()
    print(n - k)
    print(*path)
else:

    queue = deque([n])
    dist = [-1] * (2 * k + 1)
    moved = [-1] * (2 * k + 1)

    dist[n] = 0

    while queue:
        x = queue.popleft()

        if k == x:
            px = x
            path.append(k)
            while moved[px] != -1:
                path.append(moved[px])
                px = moved[px]
            path.reverse()
            print(dist[k])
            print(*path)
            break
                

        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < (2 * k + 1):
                if dist[nx] == -1:
                    dist[nx] = dist[x] + 1
                    moved[nx] = x
                    queue.append(nx)
                else:
                    if dist[nx] > dist[x] + 1:
                        dist[nx] = dist[x] + 1
                        moved[nx] = x