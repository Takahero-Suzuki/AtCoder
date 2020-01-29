import collections
N=int(input())
li=[]
for n in range(N):
    A=int(input())
    li.append(A)
li_count=collections.Counter(li)
ans=0
for k in li_count.keys():
    if li_count[k]%2!=0:
        ans+=1
print(ans)
