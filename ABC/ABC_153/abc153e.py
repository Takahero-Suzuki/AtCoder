H,N = map(int,input().split())
magic = [list(map(int,input().split())) for i in range(N)]

INF = 10**9

dp = [INF for i in range(H+1)]
dp[0] = 0

for i in range(1,H+1):
    for j in range(N):
        dp[i] = min(dp[max(0,i-magic[j][0])]+magic[j][1],dp[i])
print(dp[H])
