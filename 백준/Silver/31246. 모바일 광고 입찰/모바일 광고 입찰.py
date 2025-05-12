import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = list()
for i in range(n):
    a, b = map(int, input().split())
    if b - a < 0: 
        lst.append(0)
    else:
        lst.append(b - a)
lst.sort()
print(lst[k - 1])