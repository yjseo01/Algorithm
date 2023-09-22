import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(lambda x:ord(x)-65, input())) for _ in range(r)]
visited = [False] * 26
max_length = 1
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, cnt):
    global max_length
    max_length = max(max_length, cnt)

    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]

        if 0 <= nx < r and 0 <= ny < c:
            if not visited[board[nx][ny]]:
                visited[board[nx][ny]] = True
                dfs(nx, ny, cnt + 1)
                visited[board[nx][ny]] = False

visited[board[0][0]] = True
dfs(0, 0, max_length)
print(max_length)
