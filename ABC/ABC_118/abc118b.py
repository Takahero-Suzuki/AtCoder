N,M = map(int,input().split())
ans = set([str(m) for m in range(1,M+1)])
for n in range(N):
    A = input().split()
    A.pop(0)
    ans = ans & set(A)
print(len(ans))
