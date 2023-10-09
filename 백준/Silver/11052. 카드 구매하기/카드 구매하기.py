N = int(input())
p = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = p[0]

for i in range(2, N + 1):
    for j in range(1, i):
        dp[i] = max(dp[j] + p[i - j - 1], dp[i])
    dp[i] = max(dp[i], p[i - 1])

print(dp[N])