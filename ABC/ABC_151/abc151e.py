def modinv2(a,m):
    return pow(a,m-2,m)

def modcomn(n,r,m):
    modcom = [0 for _ in range(n)]
    for i in range(n):
        if i < r-1:
            continue
        if i == r-1:
            modcom[i] = 1
        elif i == r:
            modcom[i] = (i+1)%m
        else:
            div = modinv2(i-r+1,m)
            modcom[i] = (modcom[i-1]*div%m)*(i+1)%m
    return modcom

N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
P = 10**9+7

com = modcomn(N-1,K-1,P)

ans = 0

for i in range(N):
    if i >= K-1:
        ans = (ans+A[i]*com[i-1]%P)%P

A.sort(reverse=True)
for i in range(N):
    if i >= K-1:
        ans = (ans-A[i]*com[i-1]%P)%P

print(ans)
