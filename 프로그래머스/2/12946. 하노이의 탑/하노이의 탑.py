def hanoi(x, start, end, answer):
    if x == 1:
        answer.append([start, end])
        return
    
    hanoi(x - 1, start, 6 - start - end, answer)
    answer.append([start, end])
    hanoi(x - 1, 6 - start - end, end, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, answer)
    return answer