import sys
sys.setrecursionlimit(10 ** 7)

def add_star(length):
    if length == 1:
        return ['*']

    stars = add_star(length // 3)
    lst = []

    for s in stars:
        lst.append(s * 3)
    for s in stars:
        lst.append(s + ' ' * (length // 3) + s)
    for s in stars:
        lst.append(s * 3)

    return lst

n = int(input())
print('\n'.join(add_star(n)))