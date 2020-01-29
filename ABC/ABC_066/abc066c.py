N=int(input())
li=list(map(int,input().split()))
if N%2==0:
    ans_normal=li[::2]
    ans_rev=li[1::2]
else:
    ans_rev=li[::2]
    ans_normal=li[1::2]  
ans_rev.reverse()
ans=ans_rev+ans_normal
for n in range(N):
    ans[n]=str(ans[n])
print(' '.join(ans))
