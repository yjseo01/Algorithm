import sys
sys.setrecursionlimit(10 ** 7)

def quad_tree(n, x, y):
    check = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if video[i][j] != check:
                print('(', end='')
                for l in range(2):
                    for k in range(2):
                        quad_tree(n // 2, x + l * (n // 2), y + k * (n // 2))
                print(')', end='')
                return
    print(check, end = '')

N = int(input())
video = [[int(num) for num in input()] for _ in range(N)]
quad_tree(N, 0, 0)
