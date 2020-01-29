N = int(input())
a = list(map(int,input().split()))
ans1 = 0
ans2 = 0
S1 = 0
S2 = 0
for n in range(N):
    S1 += a[n]
    S2 += a[n]
    if n%2 == 0:
        if S1 >= -1:
            ans1 += S1 + 1
            S1 = -1
        if S2 <= 1:
            ans2 += 1 - S2
            S2 = 1
    if n%2 == 1:
        if S1 <= 1:
            ans1 += 1 - S1
            S1 = 1
        if S2 >= -1:
            ans2 += S2 + 1
            S2 = -1
print(min(ans1,ans2))
