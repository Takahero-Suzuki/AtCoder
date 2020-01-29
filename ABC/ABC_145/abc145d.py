#拡張ユークリッド互除法
#ax+by=1の1つの解(gcd(a,b)=1)
#仕組みをちゃんと理解していない
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def modinv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m #負の値を返さないように

X,Y = map(int,input().split())

X,Y = min(X,Y),max(X,Y)

if (X+Y)%3 != 0 or X*2-Y < 0:
    ans = 0
else:
    a = (2*X-Y)//3
    b = (2*Y-X)//3
    m = 10**9+7
    ans = 1
    for i in range(b+1,a+b+1):
        ans = ans*i%m
    for i in range(1,a+1):
        ans = ans*modinv(i,m)%m
print(ans)

'''
#コンテスト中の解法
X,Y = map(int,input().split())
P = 10**9 + 7
#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

if (X+Y)%3 != 0:
    ans = 0
elif min(X,Y)*2 < max(X,Y):
    ans = 0
else:
    A = (min(X,Y)-abs(X-Y))//3+abs(X-Y)
    B = (min(X,Y)-abs(X-Y))//3
    ans = 1
    for i in range(A):
        ans = ans*(A+B-i)%P
    for i in range(1,A+1):
        ans = ans*mod_inv(i,P)%P
print(ans)

'''