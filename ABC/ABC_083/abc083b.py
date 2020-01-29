N,A,B=map(int,input().split())
s=0
for n in range(1,N+1):
  a=sum(list(map(int,str(n))))
  if A<=a<=B:
    s+=n
print(s)

