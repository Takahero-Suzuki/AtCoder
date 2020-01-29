N=int(input())
c='No'
for n in range(1,10):
    if N%n==0 and 1<=N//n<=9:
        c='Yes'
        break
print(c)