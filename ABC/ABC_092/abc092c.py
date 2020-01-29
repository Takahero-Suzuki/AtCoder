N=int(input())
A=list(map(int,input().split()))
A.append(0)
S=0
a=[]
c=[]
f=0

for n in range(N):
    S+=abs(A[n]-f)
    a.append(abs(A[n]-f))
    c.append(abs(A[n+1]-f))
    f=A[n]

S+=abs(A[n])
a.append(abs(A[n]))

for n in range(N):
    print(S-a[n]-a[n+1]+c[n])
