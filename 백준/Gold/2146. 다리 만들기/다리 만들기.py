import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 섬에 번호 붙이기
def dfs(x, y, idx): # 섬일 때 좌표, 섬 번호
    graph[x][y] = idx # 방문 처리

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = idx # 방문 처리
            dfs(nx, ny, idx)


# 섬 사이의 최단거리 구하기
def bfs(graph, n): # graph, 섬 번호
    check = [[-1] * N for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j] == n:
                queue.append((i, j))
                check[i][j] = 0 # 바다는 -1, 섬은 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] > 0 and graph[nx][ny] != n: # 다른 섬 도착
                return check[x][y]

            if graph[nx][ny] == 0 and check[nx][ny] == -1 : # 방문 x 바다
                check[nx][ny] = check[x][y] + 1 # 다리 길이 1 증가
                queue.append((nx, ny))

    return 2 * N


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rsplit())))

# 섬에 번호 붙이기
idx = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j, idx)
            idx += 1

# 섬 사이 최단거리 구하기
ans = 2 * N
for i in range(2, idx):
    ans = min(ans, bfs(graph, i))

print(ans)
