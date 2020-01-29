N,K,S = map(int,input().split())

if S == 10**9:
    ans = [10**9-1 for i in range(N)]
else:
    ans = [10**9 for i in range(N)]

for i in range(K):
    ans[i] = S

print(' '.join(map(str,ans)))
