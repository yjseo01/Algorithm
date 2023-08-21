import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

inputs = []
for _ in range(V):
    inputs = list(map(int, input().rsplit()))
    num = inputs[0]
    for i in range(1, len(inputs) - 1, 2):
        graph[num].append((inputs[i], inputs[i + 1]))

def dfs(v, w): # w는 시작 정점에서부터 v정점까지의 거리
    for a, b in graph[v]:
        if visited[a] == -1: # 방문하지 않은 정점
            visited[a] = w + b # 시작 정점에서부터 a정점까지 거리
            dfs(a, w + b)

# 임의의 정점 x에서 가장 멀리 떨어져 있는 정점 y
visited = [-1] * (V + 1)
visited[1] = 0
dfs(1, 0)
y = visited.index(max(visited))

# 임의의 정점 y에서 가장 멀리 떨어져 있는 정점 z
visited = [-1] * (V + 1)
visited[y] = 0
dfs(y, 0)

# 정점 y에서 정점 z까지의 거리
print(max(visited))
