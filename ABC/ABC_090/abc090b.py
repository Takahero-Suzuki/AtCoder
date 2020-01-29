A,B=map(int,input().split())
count=0
while A<=B:
  li=list(map(int,str(A)))
  if li[0]==li[4] and li[1]==li[3]:
    count+=1
  A+=1
print(count)