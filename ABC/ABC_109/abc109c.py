import fractions
 
N,X = map(int,input().split())
x = list(map(int,input().split()))
 
for n in range(N):
    x[n] = abs(x[n]-X)

if N == 1:
    ans = x[0]

else:
    ans = fractions.gcd(x[0],x[1])
    for n in range(2,N):
        ans = fractions.gcd(ans,x[n])

print(ans)