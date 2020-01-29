N = int(input())
W = list(map(int,input().split()))

S1 = W[0]
S2 = sum(W)-W[0]
ans = abs(S1-S2)

for i in range(1,N):
    S1 += W[i]
    S2 -= W[i]
    ans = min(ans,abs(S1-S2))

print(ans)
