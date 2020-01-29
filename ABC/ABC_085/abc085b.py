N=int(input())
d=[]
for n in range(N):
  x=int(input())
  d.append(x)
ans=sorted(set(d), key=d.index)
print(len(ans))
