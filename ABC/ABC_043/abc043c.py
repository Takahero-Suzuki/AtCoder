N=int(input())
li=list(map(int,input().split()))
ave1=sum(li)//N
ave2=sum(li)//N+1
ans1=0
ans2=0
for n in range(len(li)):
  ans1+=(li[n]-ave1)**2
  ans2+=(li[n]-ave2)**2
print(min(ans1,ans2))