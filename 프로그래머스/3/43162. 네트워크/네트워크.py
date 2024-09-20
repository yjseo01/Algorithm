def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(x):
        if visited[x] == 1:
            return
        else:
            visited[x] = 1
        
        for i in range(n):
            if computers[x][i] == 1 and visited[i] == 0:
                dfs(i)
                
        return 
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    
    return answer