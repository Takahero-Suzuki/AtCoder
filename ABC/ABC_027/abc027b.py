N = int(input())
A = list(map(int,input().split()))
S = sum(A)
if S%N != 0:
    ans = -1
else:
    ans = 0
    a = S//N
    f = 0
    n = 0
    for i in range(N):
        if (n+A[i]) != a*(i+1-f):
            ans += 1
            n += A[i]
        else:
            f = i+1
            n = 0

print(ans)
