import sys
input = sys.stdin.readline

t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    su1 = set(map(int, input().split()))
    m = int(input())
    su2 = list(map(int, input().split()))

    for i in su2:
        if i in su1:
            print(1)
        else:
            print(0)