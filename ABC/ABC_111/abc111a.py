n=int(input())
li=list(map(int,str(n)))
for n in range(3):
    if li[n]==1:
        li[n]=9
    elif li[n]==9:
        li[n]=1
print(li[0]*100+li[1]*10+li[2])
