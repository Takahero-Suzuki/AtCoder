N,D = map(int,input().split())
X = [list(map(int,input().split())) for i in range(N)]

ans = 0

for i in range(N):
    for j in range(i):
        d = 0
        for k in range(D):
            d += (X[i][k]-X[j][k])**2
        dsqrt = d**0.5
        if dsqrt == dsqrt//1:
            ans += 1 
print(ans)
