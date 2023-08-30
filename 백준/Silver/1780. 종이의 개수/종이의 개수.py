import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().rsplit())) for _ in range(N)]

count = [0] * 3

def recursion(n, x, y):
    global count
    check = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if matrix[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        recursion(n // 3, x + k * n // 3, y + l * n // 3)
                return

    count[check + 1] += 1

recursion(N, 0, 0)
for i in count:
    print(i)