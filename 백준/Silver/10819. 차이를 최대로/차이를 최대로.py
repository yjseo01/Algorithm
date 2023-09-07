from itertools import permutations

def calcfunc(lst):
    res = 0
    for i in range(len(lst) - 1):
        res += abs(lst[i] - lst[i + 1])
    return res

n = int(input())
arr = list(map(int, input().split()))
parr = list(permutations(arr, n))

ans = -1e9
for lst in parr:
    ans = max(ans, calcfunc(lst))

print(ans)