import sys
import math
input = sys.stdin.readline

def length(P1, P2): # 두 점 사이의 거리를 구하는 함수
    return math.sqrt(pow(P1[0] - P2[0], 2) + pow(P1[1] - P2[1], 2))

inputs = list(map(int, input().rsplit()))
A = [inputs[0], inputs[1]]
B = [inputs[2], inputs[3]]
C = [inputs[4], inputs[5]]
D = [inputs[6], inputs[7]]

start1 = A
start2 = C
end1 = B
end2 = D

cnt = 100 # 실행횟수
ans = 0

while cnt > 0:
    AB1 = [(end1[0] + 2 * start1[0]) / 3, (end1[1] + 2 * start1[1]) / 3] # A, B의 1:2 내분점
    AB2 = [(2 * end1[0] + start1[0]) / 3, (2 * end1[1] + start1[1]) / 3] # A, B의 2:1 내분점
    CD1 = [(end2[0] + 2 * start2[0]) / 3, (end2[1] + 2 * start2[1]) / 3] # C, D의 1:2 내분점
    CD2 = [(2 * end2[0] + start2[0]) / 3, (2 * end2[1] + start2[1]) / 3] # C, D의 2:1 내분점

    f1 = length(AB1, CD1)
    f2 = length(AB2, CD2)

    if f1 <= f2: # f(mid1) <= f(mid2) 이면 mid2부터 end까지 최솟값 존재 x
        end1 = AB2
        end2 = CD2
    else: # f(mid1) > f(mid2) 이면 start부터 mid1까지 최솟값 존재 x
        start1 = AB1
        start2 = CD1

    ans = min(f1, f2)
    cnt -= 1

print(ans)
