import sys
input = sys.stdin.readline

def solve(N, arr):
    answer = 0
    arr.sort()

    for i in range(N - 1, -1, -1):
        start, end = 0, N - 1

        while start < end:
            if start == i:
                start += 1
                continue
            elif end == i:
                end -= 1
                continue

            add = arr[start] + arr[end]
            
            if add == arr[i]:
                answer += 1
                break
            elif add > arr[i]:
                end -= 1
            else:
                start += 1
            
    return answer

N = int(input())
arr = list(map(int, input().split()))

print(solve(N, arr))