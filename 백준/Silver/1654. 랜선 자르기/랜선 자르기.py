import sys
input = sys.stdin.readline

K, N = map(int, input().rsplit())
lst = []
for _ in range(K):
    lst.append(int(input()))

high = max(lst) # 가능한 최대 길이
low = 1
mid = 0
while low <= high:
    mid = (high + low) // 2

    cnt = 0 # 랜선의 개수
    for elem in lst:
        cnt += elem // mid

    if cnt >= N: # 개수보다 적거나 같게 만드는 경우
        low = mid + 1
    else:
        high = mid - 1

print(high)