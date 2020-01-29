N=int(input())

li=list(map(int,input().split()))
ans=0
for n in range(N):
  for k in range(n):
    ans+=li[n]*li[k]
print(ans)