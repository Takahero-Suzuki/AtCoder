N,M,X,Y = map(int,input().split())
x = max(list(map(int,input().split())))
y = min(list(map(int,input().split())))
ans = 'War'
for Z in range(X+1,Y+1):
    if x < Z <= y:
        ans = 'No War'
        break
print(ans)