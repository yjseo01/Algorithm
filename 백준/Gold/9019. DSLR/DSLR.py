from collections import deque
import sys
input = sys.stdin.readline

# DSLR 계산 함수
def calcD(n):
    if n * 2 > 9999:
        return (n * 2) % 10000
    else:
        return n * 2

def calcS(n):
    if n == 0:
        return 9999
    else:
        return n - 1

def calcL(n):
    n = str(n)

    if len(n) == 1:
        n = '000' + n
    elif len(n) == 2:
        n = '00' + n
    elif  len(n) == 3:
        n = '0' + n

    tmp = n[0]
    n = n[1:] + tmp
    n = int(n)
    return n

def calcR(n):
    n = str(n)

    if len(n) == 1:
        n = '000' + n
    elif len(n) == 2:
        n = '00' + n
    elif  len(n) == 3:
        n = '0' + n

    tmp = n[3]
    n = tmp + n[:3]
    n = int(n)
    return n

# BFS
def BFS(a, b):
    queue = deque([(a, "")]) # 노드, path
    # visited 배열 초기화
    visited = [0] * 10000
    visited[a] = 1
    # 부모 노드를 저장할 딕셔너리
    parent = {}

    while queue:
        x, path = queue.popleft()
        if x == b:
            return path

        # 자식 노드
        dx = [calcD(x), calcS(x), calcL(x), calcR(x)]

        for i in range(4):
            if not visited[dx[i]]:
                visited[dx[i]] = 1
                queue.append((dx[i], path + path_letters[i]))
                parent[dx[i]] = (x, path_letters[i])

    return ""

path_letters = ["D", "S", "L", "R"]

T = int(input())
for _ in range(T):
    a, b = map(int, input().rsplit())
    path = BFS(a, b)
    print(path)
