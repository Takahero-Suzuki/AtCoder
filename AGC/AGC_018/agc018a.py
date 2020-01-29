def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def gcdlist(l):
    a = l[0]
    for i in range(1,len(l)):
        a = gcd(a,l[i])
    return a

N,K = map(int,input().split())
A = list(map(int,input().split()))

g = gcdlist(A)
M = max(A)
if K > M:
    ans = 'IMPOSSIBLE'
elif K%g == 0:
    ans = 'POSSIBLE'
else:
    ans = 'IMPOSSIBLE'

print(ans)
