import sys
input = sys.stdin.readline

cnt = 0

def backtracking(idx, sum):
    global cnt

    if idx >= n:
        return

    sum += num[idx]

    if sum == s:
        cnt += 1

    backtracking(idx + 1, sum)
    backtracking(idx + 1, sum - num[idx])

n, s = map(int, input().rsplit())
num = list(map(int, input().split()))

backtracking(0, 0)

print(cnt)
