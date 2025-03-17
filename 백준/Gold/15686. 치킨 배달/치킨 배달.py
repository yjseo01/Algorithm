import sys
input = sys.stdin.readline

n, m = map(int, input().split())
min_ans = 99999999
home = []
chicken = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

visited = [False] * len(chicken)

def dfs(idx, cnt):
    global min_ans

    if cnt == m:
        ans = 0
        for hx, hy in home:
            distance = 99999999
            for j in range(len(visited)):
                if visited[j]:
                    cx, cy = chicken[j]
                    check_num = abs(hx - cx) + abs(hy - cy)
                    distance = min(distance, check_num)
            ans += distance
        min_ans = min(min_ans, ans)
        return
    
    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False

dfs(0, 0)
print(min_ans)
