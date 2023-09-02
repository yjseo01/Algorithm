n, m, k = map(int, input().split())
student = n + m
team = 0
while n >= 2 and m >= 1:
    if student - 3 * (team + 1) >= k:
        team += 1
        n, m = n - 2, m - 1
    else:
        break

print(team)
