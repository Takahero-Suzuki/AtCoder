def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

A = int(input())
B = int(input())
N = int(input())

l = lcm(A,B)
ans = l

while ans < N:
    ans += l

print(ans)
 