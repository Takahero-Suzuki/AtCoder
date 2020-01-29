N,M=map(int,input().split())
ans=1
if abs(N-M)>=2:
    print(0)
elif abs(N-M)==1:
    for n in range(N):
        ans*=(n+1)
        ans%=1000000007
    for m in range(M):
        ans*=(m+1)
        ans%=1000000007
    print(ans)
else:
    for n in range(N):
        ans*=(n+1)
        ans%=1000000007
    for m in range(M):
        ans*=(m+1)
        ans%=1000000007
    ans*=2
    ans%=1000000007
    print(ans)
