from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(i, j):
    queue = deque([(i, j, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True

    while queue:
        x, y, cnt = queue.popleft()

        if matrix[x][y] == 1:
            return cnt

        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                queue.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
    
    return float('inf')  # 1에 도달하지 못한 경우

ans = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] != 1:
            ans = max(bfs(i, j), ans)

print(ans)
