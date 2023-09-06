import sys
input = sys.stdin.readline

n = int(input())
m = int(input()) # 고장난 버튼의 개수
broken = list(map(int, input().rsplit())) # 고장난 버튼 리스트

count = abs(n - 100)

# n과 가장 가까운 숫자 i 찾기
for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        if int(i[j]) in broken: # 숫자 i 안에 망가진 버튼이 있음
            break
        elif j == len(i) - 1: # i가 n과 지금까지 가장 가까운 버튼인지 확인하고 업데이트
            count = min(count, abs(int(i) - n) + len(i))

print(count)