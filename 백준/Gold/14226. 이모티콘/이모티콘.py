from collections import deque
import sys
input = sys.stdin.readline

s = int(input())

queue = deque([(1, 0)])
dist = [[-1] * 2000 for _ in range(2000)]
dist[1][0] = 0

while queue:
    x, c = queue.popleft()

    # 클립보드 저장
    if dist[x][x] == -1:
        dist[x][x] = dist[x][c] + 1
        queue.append((x, x))

    # 화면
    nx = x + c
    if 0 <= nx < 2000 and dist[nx][c] == -1:
        dist[nx][c] = dist[x][c] + 1
        queue.append((nx, c))
    
    nx = x - 1
    if 0 <= nx < 2000 and dist[nx][c] == -1:
        dist[x - 1][c] = dist[x][c] + 1
        queue.append((nx, c))

ans = -1
for i in range(2000):
    if dist[s][i] != -1:
        if ans == -1 or dist[s][i] < ans:
            ans = dist[s][i]

print(ans)