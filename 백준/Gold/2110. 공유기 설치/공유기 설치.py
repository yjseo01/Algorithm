import sys
input = sys.stdin.readline

N, C = map(int, input().rsplit())
homes = []
for _ in range(N):
    homes.append(int(input()))

homes.sort()

start = 1 # 집 사이 최소 거리
end = homes[N - 1] - homes[0] # 집 사이 최대 거리
mid = 0
result = 0 # 답

if C == 2:
    print(homes[N - 1] - homes[0])
    exit()

while start <= end:
    mid = (start + end) // 2

    count = 1 # 공유기의 개수
    x = homes[0] # 마지막으로 설치된 공유기의 위치

    for i in range(N):
        if homes[i] - x >= mid: # 현재 집에서 다음 집의 거리가 mid 초과
            count += 1
            x = homes[i]

    if count >= C: # 간격을 늘려야 함
        result = mid
        start = mid + 1
    else: # 간격을 좁혀야 함
        end = mid - 1

print(result)