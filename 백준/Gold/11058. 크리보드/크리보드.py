n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[1] = 1

    if n > 1:
        dp[2] = 2
    if n > 2:
        dp[3] = 3

    for i in range(4, n + 1):
        for j in range(1, i - 1):
            dp[i] = max(dp[i], dp[i - 1] + 1, dp[j] * (i - j - 1))

    print(dp[n])