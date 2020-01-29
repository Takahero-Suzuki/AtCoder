# PyPyしか通らず…
import itertools

H,W = map(int,input().split())
cost = [list(map(int,input().split())) for _ in range(10)]
A = [list(map(int,input().split())) for _ in range(H)]


to1 = [10**3 for i in range(10)]

nlist = [0] + [i for i in range(2,10)]

for i in range(1,10):
    for v in itertools.permutations(nlist,i):
        c = 0
        for j in range(i-1):
            c += cost[v[j]][v[j+1]]
        c += cost[v[i-1]][1]
        to1[v[0]] = min(to1[v[0]], c)

ans = 0
for h in range(H):
    for w in range(W):
        if A[h][w] != 1 and A[h][w] != -1:
            ans += to1[A[h][w]]

print(ans)

        
