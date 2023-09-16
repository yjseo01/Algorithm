from collections import deque
import sys
input = sys.stdin.readline

volumes = tuple(map(int, input().rsplit()))

def carryWater(idx1, idx2, n): # 물 옮기는 함수
    next = list(n)
    if next[idx1] <= volumes[idx2] - next[idx2]: # idx1번 물통이 빔
        next[idx2] += next[idx1]
        next[idx1] = 0
    elif next[idx2] + next[idx1] >= volumes[idx2]: # idx2번 물통이 가득 참
        next[idx1] -= volumes[idx2] - next[idx2]
        next[idx2] = volumes[idx2]

    return tuple(next)

def BFS():
    bottles = (0, 0, volumes[2])
    queue = deque([(bottles)])
    visited = set()
    visited.add(bottles)

    answer = []

    while queue:
        node = queue.popleft()

        if node[0] == 0: # a 뭍통이 비었을 경우
            answer.append(node[2])

        # i번째 물통에서 j번째 물통으로 물 옮기기
        for i in range(3):
            for j in range(3):
                if i != j and node[i] > 0 and node[j] < volumes[j]:
                    newnode = carryWater(i, j, node)
                    if newnode not in visited:
                        visited.add(newnode)
                        queue.append(newnode)

    answer.sort()
    return answer

ans = BFS()
for i in ans:
    print(i, end=' ')