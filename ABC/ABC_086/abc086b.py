import math
s=input().split()
X=int(s[0]+s[1])
root=math.sqrt(X)
a=root//1
if a!=root:
  print('No')
else:
  print('Yes')