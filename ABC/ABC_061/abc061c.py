N,K=map(int,input().split())
ans={}
for n in range(N):
  a,b=map(int,input().split())
  if a in ans.keys():
    ans[a]+=b
  else:
    ans[a]=b
answer=sorted(ans.items(), key=lambda x:x[0])
count=0
for k in range(len(answer)):
  count+=answer[k][1]
  if count>=K:
    print(answer[k][0])
    break

