from collections import deque
N,M = map(int,input().split())
ans = deque([i for i in range(1,N+1)])
check = {i:0 for i in range(1,N+1)}
for m in range(M):
    ans.appendleft(int(input()))
while N > 0:
    if check[ans[0]] == 0:
        check[ans[0]] = 1
        print(ans.popleft())
        N -= 1
    else:
        ans.popleft()
