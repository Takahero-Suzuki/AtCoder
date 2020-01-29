N,Q = map(int,input().split())
a = [0 for n in range(N)]
for q in range(Q):
    L,R,T = map(int,input().split())
    for p in range(L-1,R):
        a[p] = T
for n in range(N):
    print(a[n])
