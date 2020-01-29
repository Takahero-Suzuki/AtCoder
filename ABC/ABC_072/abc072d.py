N = int(input())
p = list(map(int,input().split()))
ans = 0
c = 0
for i in range(N):
    if p[i] == i+1:
        c += 1
    else:
        ans += (c+1)//2
        c = 0
print(ans+(c+1)//2)

N = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    if p[i] == i+1:
        p[i],p[i+1] = p[i+1],p[i]
        ans += 1
if p[N-1] == N:
    ans += 1
print(ans)