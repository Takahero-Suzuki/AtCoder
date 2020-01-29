numbers=list(map(int,input().split()))
numbers.sort()
A,B,C=numbers
if (B-A)%2==0:
    print((C-B)+(B-A)//2)
else:
    print((C-B)+(B-A+1)//2+1)
    