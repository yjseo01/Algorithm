def solution(name):
    answer = 0
    for n in name:
        alphabet = ord(n) - 65
        answer += min(alphabet, 26 - alphabet)
    
    move = len(name) - 1
    for i in range(len(name)):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        move = min(move, 2 * i + len(name) - next_i, 2 * (len(name) - next_i) + i)
    
    answer += move

    return answer