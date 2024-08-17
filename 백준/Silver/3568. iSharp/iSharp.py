import sys
input = sys.stdin.readline

valtypelst = [ '[', ']', '&', '*' ]

inputstr = input()
valtype = ''
for i in range(len(inputstr)):
    if inputstr[i] != ' ':
        valtype += inputstr[i]
    else:
        break
valname = list(inputstr[len(valtype) + 1: -2].split(', '))
for i in range(len(valname)):
    ans = ''
    valnm = ''
    for c in valname[i]:
        if c in valtypelst:
            if c != '[' and c != ']':
                ans = c + ans
            elif  c == '[':
                ans =  ']' + ans
            elif c == ']':
                ans = '[' + ans
        else:
            valnm += c
    ans = valtype + ans + ' ' + valnm + ';'
    print(ans)
