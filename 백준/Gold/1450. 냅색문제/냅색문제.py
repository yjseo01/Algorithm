import sys
import bisect
from itertools import combinations
input = sys.stdin.readline

def get_sub_sum(weights):
    result = []
    wlen = len(weights)

    for i in range(wlen + 1):
        combs = combinations(weights, i)
        for comb in combs:
            result.append(sum(comb))

    return result

def solve(N, C, weights):
    # meet in the middle
    # 1) 물건을 절반으로 나눔
    left = weights[:N//2]
    right = weights[N//2:]

    # 2) 각 절반에 대해 가능한 모든 무게 합의 조합 구하기
    left_sum = get_sub_sum(left)
    right_sum = get_sub_sum(right)
    right_sum.sort() # 이분탐색 사용을 위해 정렬

    # 3) 이분 탐색으로 왼쪽 무게 합 + 오른쪽 무게 합 <= C인 경우 찾기
    count = 0
    for lsum in left_sum:
        count += bisect.bisect_right(right_sum, C - lsum)
    
    return count

N, C = map(int, input().split())
weights = list(map(int, input().split()))

print(solve(N, C, weights))