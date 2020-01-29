N=int(input())
d={}
ans=0
for n in range(N):
    S=input()
    if S in d:
        d[S]+=1
    else:
        d[S]=1
M=int(input())
for m in range(M):
    T=input()
    if T in d:
        d[T]-=1
    else:
        d[T]=1
for k in d:
    if d[k]>ans:
        ans=d[k]
print(ans)
