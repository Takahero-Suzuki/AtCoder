N,K,M = map(int,input().split())
A = list(map(int,input().split()))

w = M*N-sum(A)

if w > K:
    print(-1)
else:
    print(max(w,0))


