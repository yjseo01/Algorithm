import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = 1

    count = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                count += dfs(nx, ny)
    
    return count

ans = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            ans.append(dfs(i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)