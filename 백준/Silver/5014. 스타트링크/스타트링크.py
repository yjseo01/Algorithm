from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().rsplit())

def BFS():
    queue = deque([(s, 0)]) # 시작 층(s), 이동한 횟수(0)
    visited = [0] * (f + 1)
    visited[s] = 1 # s층 방문 처리

    while queue:
        x, depth = queue.popleft()

        if x == g: # g층에 도달한 경우
            print(depth)
            return

        nx, mx = x + u, x - d

        if nx <= f and not visited[nx]: # 위로 u층만큼 올라가는 경우
            visited[nx] = 1
            queue.append((nx, depth + 1))

        if mx > 0 and not visited[mx]: # 아래로 d층만큼 내려가는 경우
            visited[mx] = 1
            queue.append((mx, depth + 1))

    print("use the stairs")
    return

BFS()