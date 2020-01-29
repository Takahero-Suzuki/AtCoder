c=[list(map(int,input().split()))for i in range(3)]

a1=c[1][0]-c[0][0]
a2=c[1][1]-c[0][1]
a3=c[1][2]-c[0][2]
b1=c[2][0]-c[1][0]
b2=c[2][1]-c[1][1]
b3=c[2][2]-c[1][2]

if a1==a2==a3 and b1==b2==b3 and a1%1==0 and a2%1==0 and a3%1==0 and b1%1==0 and b2%1==0 and b3%1==0:
    print('Yes')
else:
    print('No')
