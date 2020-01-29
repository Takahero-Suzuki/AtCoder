N,X = map(int,input().split())
L = list(map(int,input().split()))

ans = 1
s = 0
for i in range(N):
    s += L[i]
    if s > X:
        break
    ans += 1

print(ans)