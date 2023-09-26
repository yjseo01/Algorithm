from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
matrix = [[int(i) for i in input().strip()] for _ in range(n)]

def bfs():
    queue = deque([(0, 0, 0)]) # 세로, 가로, 벽 부순 횟수
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1 # 방문처리

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, cnt = queue.popleft()
        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1 # 방문처리
                    if matrix[nx][ny] == 1: # 방
                        queue.append((nx, ny, cnt + 1))
                    else: # 벽
                        queue.appendleft((nx, ny, cnt))
    return 0

print(bfs())