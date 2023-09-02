num = [int(i) for i in input()]

if 0 not in num:
    print(-1)
else:
    sum = 0
    for i in num:
        sum += i
    if sum % 3 == 0:
        num.sort(reverse=True)
        for i in num:
            print(i, end='')
    else:
        print(-1)
