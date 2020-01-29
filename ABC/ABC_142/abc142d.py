A,B = map(int,input().split())

#a,bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

#[[素因数,数]]を出力
def fctr1(n): 
    f=[]
    c=0
    r=int(n**0.5)
    for i in range(2,r+2):
        while n%i==0:
            c+=1
            n=n//i
        if c!=0:
            f.append([i,c])
            c=0
    if n!=1:
        f.append([n,1])
    return f

g = gcd(A,B)

print(len(fctr1(g))+1)
