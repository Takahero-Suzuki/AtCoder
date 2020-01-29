#itertoolsよりも1から2**10までbin()を使った方が速いっぽい

import itertools

N = int(input())
F = [list(map(int,input().split())) for i in range(N)]
P = [list(map(int,input().split())) for i in range(N)]

#print(F)
#print(P)

ans = -10**10
for v in itertools.product([1,0],repeat=10):
    if v != (0,0,0,0,0,0,0,0,0,0):
        bene = 0
        for i in range(N):
            c = 0
            for j in range(10):
                if v[j] == F[i][j] == 1:
                    c += 1
            bene += P[i][c]
        ans = max(ans,bene)
print(ans)
