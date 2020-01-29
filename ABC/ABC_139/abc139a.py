S=list(input())
T=list(input())
ans=0
for n in range(3):
    if S[n]==T[n]:
        ans+=1
print(ans)
