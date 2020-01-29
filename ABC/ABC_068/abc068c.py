N,M=map(int,input().split())
first=[]
second=[]
for m in range(M):
    a,b=map(int,input().split())
    if a==1:
        first.append(b)
    elif b==N:
        second.append(a)
first_and_second=set(first)&set(second)
if len(first_and_second)==0:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
