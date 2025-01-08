import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())
hour = 24
head = 0
work = 0

while hour > 0:
    if head + A <= M:
        head += A
        work += B
    else:
        head -= C
        if head < 0:
            head = 0
    
    hour -= 1

print(work)