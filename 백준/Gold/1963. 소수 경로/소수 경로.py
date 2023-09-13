import math
import sys
from collections import deque
input = sys.stdin.readline

# 소수인지 확인하는 함수 (에라토스테네스의 채)
def isPrimeNum(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def bfs(p1, p2):
    queue = deque([(p1, 0)]) # 시작 노드, 깊이

    while queue:
        x, depth = queue.popleft()

        if x == p2:
            return depth

        for i in range(4):
            for j in range(10):
                y = list(str(x))
                y[i] = str(j)
                y = int(''.join(y))
                if 1000 <= y and not visited[y] and prime[y]:
                    visited[y] = 1
                    queue.append((y, depth + 1))

    return -1

# 소수 테이블
prime = [False]
for i in range(1, 10000):
    prime.append(isPrimeNum(i))

for _ in range(int(input())):
    a, b = map(int, input().rsplit())
    visited = [0] * 10000
    visited[a] = 1
    res = bfs(a, b)

    if res == -1:
        print("Impossible")
    else:
        print(res)