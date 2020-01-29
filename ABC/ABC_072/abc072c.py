import collections
N=int(input())
li=list(map(int,input().split()))

for n in range(N):
  plus=li[n]+1
  minus=li[n]-1
  li.append(plus)
  li.append(minus)

ans=collections.Counter(li)
print(ans.most_common()[0][1])
