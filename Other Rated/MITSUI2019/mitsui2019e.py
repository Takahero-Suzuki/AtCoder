N = int(input())
A = list(map(int,input().split()))
d = [-1, -1, -1]
ans = 1
P = 10**9+7
for n in range(N):
    ans = ans*d.count(A[n]-1)%P
    if d[0] == A[n]-1:
        d[0] += 1
    elif d[1] == A[n]-1:
        d[1] += 1
    else:
        d[2] += 1
print(ans)
