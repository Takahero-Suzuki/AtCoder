N,M,A,B = map(int,input().split())
ans = 1
for m in range(M):
    c = int(input())
    if N <= A:
        N += B
    if N >= c:
        N -= c
        ans += 1
    else:
        break
if ans == M+1:
    print('complete')
else:
    print(ans)
