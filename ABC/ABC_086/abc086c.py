N=int(input())
tb=0
xb=0
yb=0
c=0
for n in range(N):
  ta,xa,ya=map(int,input().split())
  td=ta-tb
  xd=abs(xa-xb)
  yd=abs(ya-yb)
  if td>=xd+yd and (td-xd-yd)%2==0:
    tb=ta
    xb=xa
    yb=ya
  else:
    c=1
    break

if c==0:
  print('Yes')
else:
  print('No')
