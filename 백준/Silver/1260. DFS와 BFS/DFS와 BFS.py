import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i].sort()

dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)

def dfs(v):
    dfs_visited[v] = 1
    print(v, end=" ")
    
    for nv in graph[v]:
        if dfs_visited[nv] == 0:
            dfs(nv)

def bfs(v):
    bfs_visited[v] = 1

    queue = deque([v])
    while queue:
        x = queue.popleft()
        print(x, end=" ")
        
        for nx in graph[x]:
            if bfs_visited[nx] == 0:
                queue.append(nx)
                bfs_visited[nx] = 1
    
dfs(v)
print()
bfs(v)