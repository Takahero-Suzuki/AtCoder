N=int(input())
li=list(map(int,input().split()))
S=sum(li)
x=li[0]
ans=abs(S-2*x)
for n in range(1,N-1):
    x+=li[n]
    new_ans=abs(S-2*x)
    if ans>new_ans:
        ans=new_ans
print(ans)

