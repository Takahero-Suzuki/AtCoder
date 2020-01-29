N=int(input())
check=[0,0,0,0,0,0,0,0]
rate=list(map(int,input().split()))
red=0
for n in range(N):
  if 1<=rate[n]<400:
    check[0]=1
  elif 400<=rate[n]<800:
    check[1]=1
  elif 800<=rate[n]<1200:
    check[2]=1
  elif 1200<=rate[n]<1600:
    check[3]=1
  elif 1600<=rate[n]<2000:
    check[4]=1
  elif 2000<=rate[n]<2400:
    check[5]=1
  elif 2400<=rate[n]<2800:
    check[6]=1
  elif 2800<=rate[n]<3200:
    check[7]=1
  else:
    red+=1
if sum(check)==0:
  M=red
  m=1
else:
  M=sum(check)+red
  m=sum(check)
print(m,M)