S = input().split('+')
ans = 0
for s in S:
    a = list(s)
    if '0' not in a:
        ans += 1
print(ans)
