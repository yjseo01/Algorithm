import sys
input = sys.stdin.readline

def row(x, n): # 가로줄
    for i in range(9):
        if n == matrix[i][x]:
            return False
    return True

def col(y, n): # 세로줄
    for i in range(9):
        if n == matrix[y][i]:
            return False
    return True

def square(y, x, n): # 3x3 정사각형 검사
    for i in range(3):
        for j in range(3):
            if n == matrix[y // 3 * 3 + i][x // 3 * 3 + j]:
                return False
    return True

def backtracking(cnt): # 좌표
    if cnt == len(blanks):
        # 답 출력
        for i in range(9):
            for j in range(9):
                print(matrix[i][j], end=" ")
            print()
        exit()

    for i in range(1, 10):
        x, y = blanks[cnt][1], blanks[cnt][0]
        if col(y, i) and row(x, i) and square(y, x, i):
            matrix[y][x] = i
            backtracking(cnt + 1)
            matrix[y][x] = 0 # 틀린 숫자일 경우 새로운 숫자 시도 가능하도록 초기화

blanks = [] # 빈 칸의 좌표를 저장할 queue
matrix = [list(map(int, input().split())) for _ in range(9)]

for i in range(9): # 빈 칸을 모두 찾아내 queue에 저장
    for j in range(9):
        if matrix[i][j] == 0:
            blanks.append([i, j])

backtracking(0)