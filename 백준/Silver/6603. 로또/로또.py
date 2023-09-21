import sys
input = sys.stdin.readline

def backtracking(length, idx):
    if length == 6: # 로또 완성
        print(" ".join(map(str, ans)))
        return

    for i in range(idx, len(s)):
        ans.append(s[i])
        backtracking(length + 1, i + 1) # 재귀 호출
        ans.pop()


while True:
    testcase = list(map(int, input().rsplit()))
    k = testcase[0]

    if k == 0: # 입력의 마지막 줄일 경우
        exit()

    s = testcase[1:]
    s.sort()

    ans = []
    backtracking(0, 0)

    print() # 각 테스트 케이스 사이에 빈 줄 하나 출력