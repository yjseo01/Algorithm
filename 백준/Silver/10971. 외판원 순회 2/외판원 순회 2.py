import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rsplit())) for _ in range(n)]
check = int(1e9) # for pruning
visited = [0] * n

def Backtracking(depth, v, weight):
    global check

    if depth == n - 1 and graph[v][0] != 0:
        check = min(check, graph[v][0] + weight)
        return
    for i in range(n):
        if graph[v][i] > 0 and visited[i] == 0:
            visited[i] = 1
            Backtracking(depth + 1, i, weight + graph[v][i])
            visited[i] = 0

visited[0] = 1
Backtracking(0, 0, 0)

print(check)