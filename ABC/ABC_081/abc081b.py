N=int(input())
li=list(map(int,input().split()))
count=[0 for n in range(N)]
for n in range(N):
  while li[n]%2==0:
    li[n]/=2
    count[n]+=1
ans=min(count)
print(ans)

