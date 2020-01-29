N,K = map(int,input().split())
H = list(map(int,input().split()))
H.sort()
ans = 0
for i in range(max(0,N-K)):
    ans += H[i]
print(ans)
