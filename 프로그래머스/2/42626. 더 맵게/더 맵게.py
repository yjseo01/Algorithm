import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        nfood = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, nfood)
        cnt += 1
    
    answer = cnt
    return answer