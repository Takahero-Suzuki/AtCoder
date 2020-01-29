#べき乗関数powを使った逆元の計算(modinvよりもPythonでは高速、PyPyだと遅い)
def modinv(a,m):
    return pow(a,m-2,m)

#n以下の素数列挙(O(nlog(n))
def primes(n):
    ass = {}
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5)+1):
        if not is_prime[i]:
            continue
        #i**2から始めてOK
        for j in range(i*2,n+1,i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass[i] = 0
    return ass

#[[素因数,数]]を出力
def fctr1(n): 
    f = []
    c = 0
    for i in range(2,int(n**0.5)+2):
        while n%i == 0:
            c += 1
            n = n//i
        if c !=0:
            f.append([i,c])
            c = 0
    if n != 1:
        f.append([n,1])
    return f

N = int(input())
A = list(map(int,input().split()))

e = primes(10**6+7)
inv = 0
P = 10**9+7

for i in range(N):
    inv = (inv+modinv(A[i],P))%P
    l = fctr1(A[i])
    for j in range(len(l)):
        e[l[j][0]] = max(e[l[j][0]],l[j][1])

ans = 1
for k in e.keys():
    if e[k] != 0:
        for i in range(e[k]):
            ans = ans*k%P
ans = ans*inv%P

print(ans)

#解2


#a,bの最大公約数
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

#a,bの最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

#べき乗関数powを使った逆元の計算(modinvよりもPythonでは高速、PyPyだと遅い)
def modinv2(a,m):
    return pow(a,m-2,m)


N = int(input())
A = list(map(int,input().split()))
P = 10**9+7

if N == 1:
    ans = 1

else:

    inv = modinv2(A[0],P)
    g = A[0]
    invlist = []
    seki = A[0]%P

    for i in range(1,N):
        inv = (inv+modinv2(A[i],P))%P
        seki = seki*A[i]%P

    g = gcd(A[0],A[1])
    l = A[0]//g*A[1]
    cc = modinv2(g,P)
    for i in range(2,N):
        g = gcd(l,A[i])
        l = l//g*A[i]
        cc = cc*modinv2(g,P)%P

    ans = (inv*seki%P)*cc%P

print(ans)

#オイオイオイオイオイオイオイオイなんでこれで通るんだよ
#a,bの最大公約数
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

#a,bの最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

N = int(input())
A = list(map(int,input().split()))

l = A[0]
for i in range(1,N):
    l = lcm(l,A[i])

P = 10**9+7
ans = 0
for i in range(N):
    ans += l//A[i]
print(ans%P)
