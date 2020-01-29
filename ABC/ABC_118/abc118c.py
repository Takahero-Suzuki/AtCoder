import fractions
N = int(input())
A = list(map(int,input().split()))
ans = fractions.gcd(A[0],A[1])
for n in range(N-2):
    ans = fractions.gcd(ans,A[n+2])
print(ans)
