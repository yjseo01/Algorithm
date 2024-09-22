from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):  
    rectangle = [[r * 2 for r in rect] for rect in rectangle]
    characterX, characterY, itemX, itemY = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    
    def bfs():
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        queue = deque([(characterX, characterY)])
        dist = {(characterX, characterY): 0}
        
        while queue:
            x, y = queue.popleft()
            
            if x == itemX and y == itemY:
                return dist[(x, y)] // 2  
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if isValid(nx, ny):
                    if (nx, ny) not in dist:
                        dist[(nx, ny)] = dist[(x, y)] + 1
                        queue.append((nx, ny))
    
    def isValid(x, y):
        isvalid = False
        
        for rec in rectangle:
            x1, y1, x2, y2 = rec
            if x1 < x < x2 and y1 < y < y2:
                return False

            if (x == x1 or x == x2) and y1 <= y <= y2:
                isvalid = True
            elif (y == y1 or y == y2) and x1 <= x <= x2:
                isvalid = True

        return isvalid
        
    answer = bfs()
    return answer