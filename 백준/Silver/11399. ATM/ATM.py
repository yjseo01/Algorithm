n = int(input())
lst = list(map(int, input().split()))

lst.sort()
ans = 0
for i in range(n):
    add = 0
    for j in range(0, i + 1):
        add += lst[j]
    ans += add

print(ans)