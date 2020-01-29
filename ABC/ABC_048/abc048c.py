#前から2つずつ見ていき、奥側を減らすのが最適
N,x = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
for i in range(N-1):
    a = A[i]+A[i+1]
    if a > x:
        m = min(a-x,A[i+1])
        A[i+1] -= m
        ans += m
    a = A[i]+A[i+1]
    if a > x:
        A[i] -= a-x
        ans += a-x
print(ans)
