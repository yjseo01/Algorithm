import sys
input = sys.stdin.readline

n, k = map(int, input().rsplit())
a = []
for _ in range(n):
    a.append(int(input()))

cnt = 0
for i in range(n - 1, -1, -1):
    cnt += k // a[i]
    k = k % a[i]

print(cnt)