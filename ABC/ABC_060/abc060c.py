N,T=map(int,input().split())
li=list(map(int,input().split()))
ans=0
if N==1:
  print(T)
else:
  for n in range(N-1):
    if T<li[n+1]-li[n]:
      ans+=T
    else:
      ans+=li[n+1]-li[n]
  ans+=T
  print(ans)

