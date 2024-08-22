import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for x in range(0, 1000):
    for y in range(0, 1000):
        for i in (-x, x):
            for j in (-y, y):
                if a * i + b * j == c and d * i + e * j == f:
                    print(i, j)
                    exit();