import sys
input = sys.stdin.readline

n = int(input())
positive = []
negative = []
for _ in range(n):
    num = int(input())
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

result = 0

for i in range(0, len(positive), 2):
    if i == len(positive) - 1:
        result += positive[i]
        break
    if positive[i + 1] == 1:
        result += positive[i] + positive[i + 1]
    else:
        result += positive[i] * positive[i + 1]

for j in range(0, len(negative), 2):
    if j == len(negative) - 1:
        result += negative[j]
        break
    result += negative[j] * negative[j + 1]
    j += 2

print(result)
