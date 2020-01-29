N,K = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)*(N-K+1)
for i in range(N-K):
    s -= A[i]*(N-K-i)

for i in range(N-K):
    s -= A[-1-i]*(N-K-i)
print(s)
