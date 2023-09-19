import sys
input = sys.stdin.readline

def backtracking(length, idx):
    if length == l: # 암호 완성, 종료 조건
        vo, co = 0, 0 # 모음, 자음 개수

        for i in range(l): # 모음, 자음 개수 세기
            if ans[i] in vowel:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2: # 암호의 조건
            print("".join(ans))

        return

    for i in range(idx, c): # 암호 만들기
        ans.append(letters[i])
        backtracking(length + 1, i + 1) # 재귀 호출
        ans.pop()

l, c = map(int, input().rsplit())
letters = list(input().split())
letters.sort()

vowel = ['a', 'e', 'i', 'o', 'u']
ans = []
backtracking(0, 0)