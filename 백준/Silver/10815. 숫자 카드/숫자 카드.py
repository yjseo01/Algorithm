import sys
input = sys.stdin.readline


def binary_search(lst, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if lst[mid] == target:
        return mid
    if lst[mid] > target:
        return binary_search(lst, start, mid - 1, target)
    else:
        return binary_search(lst, mid + 1, end, target)


N = int(input())
lst1 = list(map(int, input().rsplit()))
M = int(input())
lst2 = list(map(int, input().rsplit()))

lst1.sort()

answer = []
for i in lst2:
    if binary_search(lst1, 0, N - 1, i) == -1:
        print(0, end=' ')
    else:
        print(1, end=' ')