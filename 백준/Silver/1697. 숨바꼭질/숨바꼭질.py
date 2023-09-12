from collections import deque

N, K = map(int, input().split())

def bfs(n, k):
    queue = deque()
    queue.append(n)
    visited = [0] * (2 * k + 1)
    visited[n] = 1
    while queue:
        x = queue.popleft()
        for y in (x - 1, x + 1, 2 * x):
            if 0 <= y <= 2 * k:
                if not visited[y]:
                    visited[y] = visited[x] + 1
                    queue.append(y)

    return visited[k] - 1

if K < N:
    print(N - K)
else:
    print(bfs(N, K))