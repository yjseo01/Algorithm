lst = [int(input()) for _ in range(5)]
avg = 0
for i in lst:
    avg += i

avg = avg // 5

lst.sort()
print(avg)
print(lst[2])