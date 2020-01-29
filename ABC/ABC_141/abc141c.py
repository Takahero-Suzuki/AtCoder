N,K,Q = map(int,input().split())
A = {i: 0 for i in range(1,N+1)}
for i in range(Q):
    a = int(input())
    A[a] += 1
for v in A.values():
    if K-Q+v > 0:
        print('Yes')
    else:
        print('No')
