import math
X=int(input())
n=math.sqrt(X)//1
while n*(n+1)<2*X:
  n+=1
print(int(n))