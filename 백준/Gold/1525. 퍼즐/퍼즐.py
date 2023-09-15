from collections import deque
import sys
input = sys.stdin.readline

def BFS(graph):
    queue = deque([graph])
    visited = dict() # 노드(퍼즐 모양): 깊이(해당 퍼즐 모양을 만들기 위한 횟수)
    visited[graph] = 0 # 몇 번째에 해당 퍼즐 모양을 방문했는지

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        node = queue.popleft()

        if node == "123456780": # 퍼즐 완성
            return visited[node]

        idx = node.find("0") # 빈공간 인덱스
        x, y = idx // 3, idx % 3 # 빈공간 좌표

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0<= ny < 3:
                nidx = nx * 3 + ny

                # 현재 빈공간이랑 빈공간 주변에 있던 숫자랑 자리 바꾸기
                newnode = list(node)
                newnode[idx] = newnode[nidx]
                newnode[nidx] = "0"
                newnode = "".join(newnode)

                if not visited.get(newnode): # 해당 퍼즐 모양을 방문한 적 없음
                    visited[newnode] = visited[node] + 1
                    queue.append(newnode)

    return -1

graph = ""
for _ in range(3):
    a, b, c = map(str, input().split())
    graph += a + b + c

print(BFS(graph))