import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

# → ↓ ↗ ↘
dx = [1, 0, 1, 1]  
dy = [0, 1, -1, 1]  

for y in range(19):
    for x in range(19):
        if board[y][x] != 0:
            color = board[y][x]
            for i in range(4):
                nx, ny, cnt = x + dx[i], y + dy[i], 1
                while cnt < 5 and 0 <= nx < 19 and 0 <= ny < 19 and board[ny][nx] == color:
                    cnt += 1
                    nx, ny = nx + dx[i], ny + dy[i]

                if cnt == 5: # 육목
                    prev_x, prev_y = x - dx[i], y - dy[i]
                    next_x, next_y = nx, ny

                    if (0 <= prev_x < 19 and 0 <= prev_y < 19 and board[prev_y][prev_x] == color):
                        continue
                    if (0 <= next_x < 19 and 0 <= next_y < 19 and board[next_y][next_x] == color):
                        continue

                    print(color)
                    print(y + 1, x + 1)
                    exit(0)

print(0)