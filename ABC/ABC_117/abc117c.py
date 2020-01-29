N,M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
X_dis = []
for m in range(M-1):
    X_dis.append(X[m+1]-X[m])
X_dis.sort()
ans = 0
if N < M:
    for i in range(M-N):
        ans += X_dis[i]
print(ans)
