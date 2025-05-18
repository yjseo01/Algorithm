import sys
input = sys.stdin.readline

def solve(N, M, cost):
    start, end = max(cost), sum(cost)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        count = 1
        remain = mid
        
        for i in cost:
            if remain < i:
                remain = mid
                count += 1
            remain -= i
        
        if count <= M:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return ans

N, M = map(int, input().split())
cost = [int(input()) for _ in range(N)]
print(solve(N, M, cost))