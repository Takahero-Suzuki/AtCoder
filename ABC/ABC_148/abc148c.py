import fractions
a,b = map(int,input().split())
g = fractions.gcd(a,b)
print(a*b//g)
