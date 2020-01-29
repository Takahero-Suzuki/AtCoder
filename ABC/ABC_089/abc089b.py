N=int(input())
li=list(input().split())
c=0
for n in range(N):
  if li[n]=='Y':
    c=1
    break
if c==0:
  print('Three')
else:
  print('Four')