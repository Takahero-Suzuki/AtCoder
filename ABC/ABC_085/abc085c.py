N,Y=map(int,input().split())

S=Y//1000-N
count=0
for x in range(N+1):
    if (S-9*x)%4==0 and (S-9*x)//4>=0 and N-x-(S-9*x)//4>=0:
        y=(S-9*x)//4
        z=N-y-x
        count=1
        break
if count==1:
    print(str(x)+' '+str(y)+' '+str(z))
else:
    print(str(-1)+' '+str(-1)+' '+str(-1))
