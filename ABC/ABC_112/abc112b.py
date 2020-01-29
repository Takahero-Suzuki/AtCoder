N,T = map(int,input().split())
ans = 10000
for n in range(N):
    c,t = map(int,input().split())
    if t <= T:
        ans = min(ans,c)
print(ans if ans != 10000 else 'TLE')