N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sA = sum(A)
for i in range(N):
    m = A[i]
    A[i] = max(0,A[i]-B[i])
    B[i] = B[i]-m+A[i]
    A[i+1] = max(0,A[i+1]-B[i])
print(sA-sum(A))
