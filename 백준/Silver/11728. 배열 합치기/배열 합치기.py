import sys
input = sys.stdin.readline

n, m = map(int, input().rsplit())
a = list(map(int, input().rsplit()))
b = list(map(int, input().rsplit()))

c = a + b
c.sort()

for i in c:
    print(i, end=' ')