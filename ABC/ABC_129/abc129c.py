from collections import deque
N,M = map(int,input().split())
a = deque([int(input()) for m in range(M)]+[-1])
ans = []
P = 10**9+7
for n in range(N):
    if n+1 == a[0]:
        ans.append(0)
        a.popleft()
    else:
        if n == 0:
            ans.append(1)
        elif n == 1:
            ans.append(ans[0]+1)
        else:
            ans.append((ans[n-1]+ans[n-2])%P)
print(ans[N-1])
