li=list(input())
ans=0
for n in range(len(li)-1):
  if li[n]!=li[n+1]:
    ans+=1
print(ans)