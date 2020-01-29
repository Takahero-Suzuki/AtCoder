N,K = map(int,input().split())
H = [int(input()) for n in range(N)]
H.sort()
ans = 10000000000
for n in range(N-K+1):
    ans = min(ans,H[n+K-1]-H[n])
print(ans)
