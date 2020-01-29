import fractions
A,B,C,D = map(int,input().split())
g = fractions.gcd(C,D)
l = C*D//g
print(B-A+1-B//C-B//D+B//l+(A-1)//C+(A-1)//D-(A-1)//l)