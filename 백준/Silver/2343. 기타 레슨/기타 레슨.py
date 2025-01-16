import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
for i in arr:
    total += i

start, end = max(arr), total # 최소 블루레이 크기, 최대 블루레이 크기
result = 0

while start <= end:
    mid = (start + end) // 2 # 블루레이 크기
    sz = mid # 남은 블루레이 공간
    cnt = 1 # 블루레이 개수

    for i in arr:
        if sz < i: # 블루레이 공간 부족
            cnt += 1
            sz = mid # 블루레이 공간 초기화
        sz -= i
    
    if cnt <= m: # 현재 크기로 m개 이하의 블루레이를 담을 수 있음
        result = mid
        end = mid - 1
    else: # 현재 크기로 m개의 블루레이를 담을 수 없음
        start = mid + 1

print(result)
