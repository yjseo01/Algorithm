import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def binary_search(lst, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if lst[mid] == target:
        return mid
    if lst[mid] > target:
        return binary_search(lst, target, start, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, end)

n = int(input())
inputs = list(map(int, input().rsplit()))
m = int(input())
checks = list(map(int, input().rsplit()))

checks2 = sorted(checks)

dic = {}
for i in checks:
    dic[i] = 0

for i in inputs:
    if binary_search(checks2, i, 0, m - 1) != -1:
        dic[i] = dic[i] + 1

for i in checks:
    print(dic[i], end=' ')
