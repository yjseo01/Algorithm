from collections import deque

def solution(begin, target, words):
    
    def bfs():
        visited = [-1] * (len(words) + 1)
        
        queue = deque([(begin, 0)])
        visited[0] = 0
        
        while queue:
            cword, idx = queue.popleft()
            
            if cword == target:
                return visited[idx]
            
            for i in range(len(words)):
                # 이동 가능한지 확인
                nword = words[i]
                cnt = 0
                for j in range(len(cword)):
                    if cword[j] != nword[j]:
                        cnt += 1
                if cnt != 1: # 이동 불가능
                    continue
                
                if visited[i + 1] == -1:
                    visited[i + 1] = visited[idx] + 1
                    queue.append((nword, i + 1))
                else:
                    visited[i + 1] = min(visited[idx] + 1, visited[i + 1])
        return 0
                    
    answer = bfs()
    
    return answer