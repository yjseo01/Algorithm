s = int(input())
an = [0]

i = 1
while an[i - 1] < s:
    an.append(an[i - 1] + i)
    i += 1

i -= 1
if an[i] != s:
    while s - an[i - 1] <= i:
        i -= 1

print(i)