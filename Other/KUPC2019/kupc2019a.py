N,X=map(int,input().split())
li=list(map(int,input().split()))

li.sort()

ans=0

for n in range(len(li)):
  if li[n]+X>=li[-1]:
    ans+=1
print(ans)
