import sys
input = sys.stdin.readline

n = int(input())
p = [0] * n
t = [0] * n

dp = [0] * (n + 1)
for i in range(n):
    t[i], p[i] = map(int, input().split())

max_val = 0

for i in range(n - 1, -1, -1):
    if (i + t[i] <= n):
        dp[i] = max(p[i] + dp[i + t[i]], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val);