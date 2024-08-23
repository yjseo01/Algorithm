import sys
input = sys.stdin.readline

x, y, z = map(int, input().split())
while x != 0 and y != 0 and z != 0:
    big = max(x, y, z)
    if x == big:
        if y * y + z * z == x * x:
            print("right")
        else:
            print("wrong")
    elif y == big:
        if x * x + z * z == y * y:
            print("right")
        else:
            print("wrong")
    elif z == big:
        if x * x + y * y == z * z:
            print("right")
        else:
            print("wrong")
    x, y, z = map(int, input().split())