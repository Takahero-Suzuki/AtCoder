N,M,X=map(int,input().split())
A=list(map(int,input().split()))
a=0
b=0
for m in range(M):
    if A[m]<X:
        a+=1
    else:
        b+=1
print(min(a,b))

