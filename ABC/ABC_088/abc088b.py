N=int(input())
li=list(map(int,input().split()))
li.sort(reverse=True)
ans=0
for n in range(N):
  if n%2==0:
    ans+=li[n]
  else:
    ans-=li[n]
print(ans)