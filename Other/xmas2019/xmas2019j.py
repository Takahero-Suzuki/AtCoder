N = int(input())

ans = 'NO'
for i in range(N):
    a,b = input().split()
    A = list(a)
    B = list(b)
    for i in range(1,len(A)+1):
        if A[(-1)*i] == B[-1]:
            B.pop(-1)
        if len(B) == 0:
            ans = 'YES'
            break

print(ans)
