import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = [0] * (n + 1)
v = [0] * (n + 1)
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    w[i], v[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= w[i]: # i번째 물건을 넣을 수 있음
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]) # max(i번째 물건을 넣지 않는 경우, i번째 물건을 넣는 경우)
        else: # i번째 물건을 넣을 수 없음
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])