import math
N=int(input())
a=math.sqrt(N)
b=int(a//1)+1
ans=10000000000000
c=0
for n in range(1,b):
    if N%n==0:
        ans=min(ans,N//n+n)
        c=1
if c==0:
    print(N-1)
else:
    print(ans-2)

