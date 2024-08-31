def solution(numbers, target):
    answer = dfs(numbers, target, 0) 
    
    return answer
        

def dfs(numbers, target, depth):
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    
    ans = 0
        
    ans += dfs(numbers, target, depth + 1)
    numbers[depth] *= -1
    ans += dfs(numbers, target, depth + 1)
    numbers[depth] *= -1
    
    return ans

    
    