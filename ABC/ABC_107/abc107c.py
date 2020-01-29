N,K = map(int,input().split())
x = list(map(int,input().split()))

ans = 10**9
for i in range(N-K+1):
    start,end = x[i],x[i+K-1]
    if end <= 0:
        ans = min(ans, abs(start)) 
    elif start <= 0:
        ans = min(ans, 2*min(abs(start), end)+max(abs(start), end))
    else:
        ans = min(ans, end)

print(ans)
