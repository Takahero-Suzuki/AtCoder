N=int(input())
s=list(input())
ans=1
for n in range(N-1):
  if s[n]!=s[n+1]:
    ans+=1
print(ans)
