N,M,C = map(int,input().split())
B = list(map(int,input().split()))
ans = 0
for n in range(N):
    A = list(map(int,input().split()))
    a = 0
    for m in range(M):
        a += A[m]*B[m]
    a += C
    if a > 0:
        ans += 1
print(ans)
