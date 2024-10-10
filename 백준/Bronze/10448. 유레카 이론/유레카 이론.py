import sys
input = sys.stdin.readline

triangle_num = []
for i in range(1, 1001):
    tnum = i * (i + 1) // 2
    triangle_num.append(tnum)

for _ in range(int(input())):
    k = int(input())
    maxnum = len(triangle_num)
    isPossible = False

    for x in range(maxnum):
        for y in range(x, maxnum):
            if triangle_num[x] + triangle_num[y] > k:
                break
            for z in range(y, maxnum):
                if triangle_num[x] + triangle_num[y] + triangle_num[z] == k:
                    isPossible = True
                    break
                if triangle_num[x] + triangle_num[y] + triangle_num[z] > k:
                    break

    if isPossible:
        print(1)
    else:
        print(0)