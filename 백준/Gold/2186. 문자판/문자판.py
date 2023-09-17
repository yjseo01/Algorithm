n, m, k = map(int, input().split())
matrix = [[s for s in input().strip()] for i in range(n)]
check_word = input().strip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[-1] * len(check_word) for _ in range(m)] for _ in range(n)]

def DFS(x, y, idx):
    if visited[x][y][idx] != -1:
        return visited[x][y][idx]

    if matrix[x][y] != check_word[idx]:
        return 0

    if idx == len(check_word) - 1:
        return 1

    cnt = 0

    for i in range(4):
        for j in range(1, k + 1):
            nx, ny = x + dx[i] * j, y + dy[i] * j

            if 0 <= nx < n and 0 <= ny < m:
                cnt += DFS(nx, ny, idx + 1)

    visited[x][y][idx] = cnt

    return cnt

ans = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == check_word[0]:
            ans += DFS(i, j, 0)

print(ans)