#a,bの最大公約数
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

N = int(input())
A = list(map(int,input().split()))

gcdf = [0 for i in range(N)]
gcdf[0] = A[0]
for i in range(1,N):
    gcdf[i] = gcd(gcdf[i-1],A[i])

#print(gcdf)

gcdb = [0 for i in range(N)]
gcdb[-1] = A[-1]
for i in range(N-2,-1,-1):
    gcdb[i] = gcd(gcdb[i+1],A[i])

#print(gcdb)

ans = max(gcdf[-2],gcdb[1])

for i in range(1,N-1):
    ans = max(ans,gcd(gcdf[i-1],gcdb[i+1]))

print(ans)
