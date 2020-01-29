import itertools
N = int(input())
ans = 0
A = []
aa = []
for n in range(N):
    a = int(input())
    aa.append(a)
    xy = [list(map(int,input().split())) for i in range(a)]
    A.append(xy)
for v in itertools.product([1,0], repeat = N):
    s = 1
    for i in range(N):
        if v[i] == 1:
            t = 1
            for j in range(aa[i]):
                if v[A[i][j][0]-1] != A[i][j][1]:
                    t = 0
                    break
            if t != 1:
                s = 0
                break
    if s == 1:
        break
print(v.count(1))


