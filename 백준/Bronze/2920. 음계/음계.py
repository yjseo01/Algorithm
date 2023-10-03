arr = list(map(int, input().split()))
ans = ""
for i in arr:
    if i - 1 == arr.index(i) and ans != "descending":
        ans = "ascending"
    elif 8 - i == arr.index(i) and ans != "ascending":
        ans = "descending"
    else:
        ans = "mixed"
        break

print(ans)
