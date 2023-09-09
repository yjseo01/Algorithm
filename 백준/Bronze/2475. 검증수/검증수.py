lst = list(map(int, input().split()))
add = 0
for i in lst:
    add += i * i

print(add % 10)
