import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

# 트리 입력 받기
for _ in range(n - 1):
    a, b, c = map(int, input().rsplit())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(v, w):
    for a, b in graph[v]:
        if visited[a] == -1:
            visited[a] = w + b # 방문 처리로 현재 노드까지의 가중치 더함
            dfs(a, w + b)


# 임의의 정점 x에서 가장 먼 정점 y
visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)
y = visited.index(max(visited))

# 정점 y에서 가장 먼 정점 z
visited = [-1] * (n + 1)
visited[y] = 0
dfs(y, 0)

# 정점 y와 정점 z사이의 거리
print(max(visited[1:]))