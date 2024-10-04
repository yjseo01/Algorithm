def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            row, col = yellow // i + 2, i + 2
            if row * col - yellow == brown:
                break
    
    answer = [row, col]
    
    return answer