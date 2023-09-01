import sys
sys.setrecursionlimit(10 ** 7)

def add_star(length):
    if length == 3:
        return ["  *  ", " * * ", "*****"]

    stars = add_star(length // 2)
    lst = []
    for s in stars:
        lst.append(" " * (length // 2) + s + " " * (length // 2))

    for s in stars:
        lst.append(s + " " + s)

    return lst

N = int(input())
print('\n'.join(add_star(N)))