import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

start, end = 0, n - 1
start_t, end_t = n - 2, n - 1
min_v = abs(lst[n - 1] + lst[n - 2])

while start < end:
    tmp = lst[start] + lst[end]

    if abs(tmp) < min_v:
        min_v = abs(tmp)
        start_t = start
        end_t = end

    if tmp > 0:
        end = end - 1
    elif tmp < 0:
        start = start + 1
    else:
        break

print(lst[start_t], lst[end_t])