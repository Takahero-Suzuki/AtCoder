N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    A[i] -= i+1

#print(A)

A.sort()

b = A[N//2]

s = 0
for i in range(N):
    s += abs(A[i]-b)

print(s)
