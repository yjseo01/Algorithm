import sys
input = sys.stdin.readline

n = int(input())

A = [0] * n
B = [0] * n
C = [0] * n
D = [0] * n

for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, input().split())

A.sort()
B.sort()
C.sort()
D.sort()

def sumlist(a, b):
    sums = [0] * (n * n)
    idx = 0
    for i in range(n):
        for j in range(n):
            sums[idx] = a[i] + b[j]
            idx += 1

    sums.sort()
    return sums


AB = sumlist(A, B)
CD = sumlist(C, D)

start, end = 0, n * n - 1
cnt = 0

while start < n * n and end >= 0:
    ABsum, CDsum = AB[start], CD[end]
    add = ABsum + CDsum

    if add < 0:
        start += 1
    elif add == 0:
        dupleAB, dupleCD = 0, 0

        while start < n * n and AB[start] == ABsum:
            dupleAB += 1
            start += 1

        while end >= 0 and CD[end] == CDsum:
            dupleCD += 1
            end -= 1

        cnt += dupleAB * dupleCD
    elif add > 0:
        end -= 1

print(cnt)