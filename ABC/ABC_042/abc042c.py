N,K=map(int,input().split())
li=list(map(int,input().split()))

N_keta=list(map(int,str(N)))

for n in range(100000):
  count=0
  for k in range(len(N_keta)):
    if N_keta[k] in li:
      count=1
      break
    
  if count==0:
    print(N)
    break
  else:
    N+=1
    N_keta=list(map(int,str(N)))

