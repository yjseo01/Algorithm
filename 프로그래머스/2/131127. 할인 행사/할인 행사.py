def solution(want, number, discount):
    answer = 0
    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
        
    for i in range(len(discount) - 9):
        discount_dic = {}
        canbuy = True
        for j in range(i, i + 10):
            if discount[j] not in discount_dic:
                discount_dic[discount[j]] = 1
            else:
                discount_dic[discount[j]] += 1
        for k in want_dic.keys():
            if k not in discount_dic or want_dic[k] > discount_dic[k]:
                canbuy = False
                break
        if canbuy:
            answer += 1
        
    return answer