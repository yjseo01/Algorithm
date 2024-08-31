from collections import deque

def solution(maps):
    answer = 0
    
    rows, cols = len(maps), len(maps[0])
    
    queue = deque([(0, 0, 0)])
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    
    while(queue):
        x, y, cnt = queue.popleft()
        
        if x == cols - 1 and y == rows - 1:
            answer = cnt
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < cols and 0 <= ny < rows:
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny, cnt + 1))
        
    if answer == 0:
        answer = -1
    else:
        answer = answer + 1
        
    return answer