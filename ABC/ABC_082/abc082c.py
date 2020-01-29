import collections
N=int(input())
li=list(map(int,input().split()))
li_count=collections.Counter(li)
li_count_most=li_count.most_common()
ans=0
for k in range(len(li_count_most)):
    if li_count_most[k][0]<=li_count_most[k][1]:
        ans+=(li_count_most[k][1]-li_count_most[k][0])
    else:
        ans+=li_count_most[k][1]
print(ans)

