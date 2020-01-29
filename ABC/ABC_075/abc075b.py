H,W=map(int,input().split())
li=[]

for h in range(H):
  s=list(input())
  li.append(s)

for h in range(H):
  for w in range(W):
    if li[h][w]=='.':
      li[h][w]=0

for h in range(H):
  for w in range(W):
    if li[h][w]=='#':
      if h!=0 and li[h-1][w]!='#':
        li[h-1][w]+=1
      if h!=H-1 and li[h+1][w]!='#':
        li[h+1][w]+=1
      if w!=0 and li[h][w-1]!='#':
        li[h][w-1]+=1
      if w!=W-1 and li[h][w+1]!='#':
        li[h][w+1]+=1
      if h!=0 and w!=0 and li[h-1][w-1]!='#':
        li[h-1][w-1]+=1
      if h!=0 and w!=W-1 and li[h-1][w+1]!='#':
        li[h-1][w+1]+=1
      if h!=H-1 and w!=0 and li[h+1][w-1]!='#':
        li[h+1][w-1]+=1
      if h!=H-1 and w!=W-1 and li[h+1][w+1]!='#':
        li[h+1][w+1]+=1

for h in range(H):
  for w in range(W):
    if li[h][w]!='#':
      li[h][w]=str(li[h][w])

for h in range(H):
  print(''.join(li[h]))
