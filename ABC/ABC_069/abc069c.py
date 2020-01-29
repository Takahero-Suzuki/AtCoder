N=int(input())
li=list(map(int,input().split()))
two_count=0
four_count=0
for n in range(N):
    if li[n]%4==0:
        four_count+=1
    elif li[n]%2==0:
        two_count+=1
S=max(four_count*2+1,four_count*2+two_count)
if S>=N:
    print('Yes')
else:
    print('No')
