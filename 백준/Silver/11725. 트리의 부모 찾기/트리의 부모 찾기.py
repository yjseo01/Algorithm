import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().rsplit())
    graph[a].append(b)
    graph[b].append(a)

#dfs
def dfs(v):
    for i in graph[v]:
        if visited[i] == 0: # 아직 방문하지 않은 노드
            visited[i] = v # i: 방문할 노드, v: i의 부모 노드
            dfs(i)

dfs(1)

for i in range(2, N + 1):
    print(visited[i])
