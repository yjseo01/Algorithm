import sys
from collections import deque
input = sys.stdin.readline

def bfs_check(start, graph, visited):
    queue = deque([start])
    visited[start] = 0  # 0번 색으로 시작

    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            # 방문하지 않았다면 현재 정점과 반대 색으로 방문
            if visited[nx] == -1:
                visited[nx] = 1 - visited[x]
                queue.append(nx)
            # 이미 방문한 정점이라면, 색이 같은지 확인
            elif visited[nx] == visited[x]:
                return False  # 같은 색이면 이분 그래프 아님
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    
    # 간선 입력
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [-1] * (v + 1)
    is_bipartite = True

    # 그래프가 여러 연결 요소로 나뉘어 있을 수 있으므로 모든 정점 체크
    for i in range(1, v + 1):
        if visited[i] == -1:
            if not bfs_check(i, graph, visited):
                is_bipartite = False
                break

    print("YES" if is_bipartite else "NO")
