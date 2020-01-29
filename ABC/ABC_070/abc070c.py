#a,bの最大公約数
def gcd(a,b):
    while b%a!=0:
        a,b=b,a%b
    return a

#a,bの最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

N=int(input())
g=int(input())
for n in range(N-1):
    t=int(input())
    g=lcm(g,t)
print(g)
