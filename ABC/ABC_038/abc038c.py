N = int(input())
A = list(map(int,input().split()))

M = 0
c = 0
ans = 0
for i in range(N):
    if A[i] <= M:
        ans += c*(c+1)//2
        c = 1
        M = A[i]
    else:
        M = A[i]
        c += 1
print(ans+c*(c+1)//2)
