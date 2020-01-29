import math
a,b,x=map(int,input().split())
if a*a*b<=2*x:
    c=(b-x/(a**2))*2/a
    ans=math.degrees(math.atan(c))
else:
    c=a*b*b/(2*x)
    ans=math.degrees(math.atan(c))
print(ans)
