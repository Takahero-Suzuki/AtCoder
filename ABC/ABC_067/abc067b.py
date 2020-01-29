N,K=map(int,input().split())

li=list(map(int,input().split()))
li.sort(reverse=True)

ans=0

for k in range(K):
  ans=ans+li[k]

print(ans)

