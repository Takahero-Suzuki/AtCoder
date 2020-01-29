import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

#a,bの最大公約数
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
#a,bの最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

N,M = map(int,readline().split())
A = list(map(int,readline().split()))

B = [A[i]//2 for i in range(N)]
ans = 1

dev_c = 0
while A[0]%2 != 1:
    A[0] = A[0]//2
    dev_c += 1
#print(dev_c)

for i in range(1,N):
    dev_c2 = 0
    while A[i]%2 != 1:
        A[i] = A[i]//2
        dev_c2 += 1
    if dev_c != dev_c2:
        ans = 0
        break

l = B[0]
if ans == 1:
    for i in range(N):
        l = lcm(l,B[i])

#print(l)

if ans != 0:
    ans = (M//l+1)//2

print(ans)