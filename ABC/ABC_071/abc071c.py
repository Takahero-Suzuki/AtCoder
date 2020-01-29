import collections

N=int(input())
li=list(map(int,input().split()))

li_count=collections.Counter(li)
a=0
b=0
for k in li_count.keys():
    if li_count[k]>=4:
        if k>a:
            a=k
        if k>b:
            b=k
    elif li_count[k]>=2 and (k>a or k>b):
        if a>=b:
            b=k
        else:
            a=k
print(a*b)
