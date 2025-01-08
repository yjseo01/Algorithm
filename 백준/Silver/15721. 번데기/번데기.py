import sys
input = sys.stdin.readline

a = int(input())
t = int(input())
g = int(input()) # 뻔: 0, 데기: 1

cnt = 0
cur = -1
n = 1

while True:
    arr = [0, 1, 0, 1]

    for _ in range(n + 1):
        arr.append(0)
    for _ in range(n + 1):
        arr.append(1)
    
    for i in range(len(arr)):
        cur = (cur + 1) % a
        if arr[i] == g:
            cnt += 1
            if cnt == t:
                print(cur)
                exit()
    n = n + 1
