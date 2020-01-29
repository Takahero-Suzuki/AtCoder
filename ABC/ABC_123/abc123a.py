li=[]
for n in range(5):
    li.append(int(input()))
li.sort()
k=int(input())
if li[4]-li[0]<=k:
    print('Yay!')
else:
    print(':(')
