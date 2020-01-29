N=int(input())
K=int(input())
x=list(map(int,input().split()))
ans=0
for n in range(N):
  if 2*x[n]<=K:
    ans+=x[n]
  else:
    ans+=K-x[n]
print(2*ans)

