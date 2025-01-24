import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = 0

    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = 1 - visited[x]
                queue.append(nx)
            elif visited[nx] == visited[x]:
                return False
            
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [-1] * (v + 1)
    is_true = True

    for i in range(1, v + 1):
        if visited[i] == -1:
            if not bfs(i, graph, visited):
                is_true = False
                break
        
    print("YES" if is_true else "NO")