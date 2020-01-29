import collections
N,K=map(int,input().split())
li=list(map(int,input().split()))
li_count=collections.Counter(li)
li_count_most=li_count.most_common()[::-1]
change=0
S=max(len(li_count)-K,0)
for s in range(S):
    change+=li_count_most[s][1]
print(change)
