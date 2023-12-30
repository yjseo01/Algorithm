n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
s_min = 0

for i in range(n):
    s_min += a[i] * b[i]

print(s_min)
