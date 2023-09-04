import sys
input = sys.stdin.readline

meetings = []
n = int(input())
for _ in range(n):
    meetings.append(tuple(map(int, input().rsplit())))

meetings.sort(key = lambda x: (x[1], -x[0]))

last = meetings[0]
if last[0] == last[1]:
    cnt = 0
else:
    cnt = 1

for i in meetings:
    if last[1] <= i[0] or last[0] >= i[1]:
        cnt += 1
        last = i

print(cnt)