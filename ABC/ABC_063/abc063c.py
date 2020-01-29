N=int(input())
li=[]

for n in range(N):
  li.append(int(input()))

li.sort()
S=sum(li)


while S%10==0 and li!=[]:
  if li[0]%10==0:
    li.pop(0)
  else:
    S-=li.pop(0)

if li==[]:
  print(0)
else:
  print(S)