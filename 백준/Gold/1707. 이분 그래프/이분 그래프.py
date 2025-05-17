import sys
sys.setrecursionlimit(20005)
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if visited[nx] != -1:
                if visited[nx] == visited[x]:
                    return False
            else:
                queue.append(nx)
                visited[nx] = 1 - visited[x]

    return True

k = int(input())
while k > 0:
    k -= 1
    
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1] * (V + 1)
    isTrue = True
    for i in range(1, V + 1):
        if visited[i] == -1:
            if not bfs(graph, visited, i):
                print("NO")
                isTrue = False
                break

    if isTrue:
        print("YES")